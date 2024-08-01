from datetime import datetime

from fastapi import WebSocket
from starlette import status
from starlette.websockets import WebSocketDisconnect

from Backend.Business.BO_student import BO_student
from Backend.WebSocket.Entity.ClientMessage import ClientMessage
from Backend.WebSocket.Entity.ResponseMessage import ResponseMessage
from Backend.WebSocket.Entity.Room_GroupTest import Room_GroupTest
from Backend.WebSocket.Entity.GroupTest_Student import GroupTest_Student
from Backend.WebSocket.Business.Room_Manager import Room_Manager
from Backend.Model.DB_model import Student
from Backend.Business.BO_authenticate import get_current_user


class BO_Student_Message:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.student = None
        self.room = None
        self.room_manager = None
        self.message = None
        self.response = None
        self.grouptest_student = None
        self.student_test = None

    async def handle(self):
        try:
            await self.websocket.accept()
            self.room_manager = Room_Manager()
            self.message = ClientMessage()
            self.response = ResponseMessage()
            self.grouptest_student = GroupTest_Student(self.websocket)

            while True:
                try:
                    msg = self.message.set_message(**await self.websocket.receive_json())
                    # COMMAND: AUTHENTICATE
                    if msg.command == ClientMessage.AUTHENTICATE:
                        self.student = await get_current_user(msg.detail['token'])
                        self.student = BO_student().get_student_by_id(self.student.id)
                        if self.student is None or not isinstance(self.student, Student):
                            self.student = None
                            await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('Invalid token').serialize())
                            continue

                        self.grouptest_student.set_student(self.student)
                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Authenticated').serialize())
                        continue

                    if self.student is None:  # check if student is authenticated
                        await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('You have not authenticated').serialize())
                        continue  # if not, continue to next loop

                    # COMMAND: JOIN GROUP TEST
                    if msg.command == ClientMessage.JOIN_GROUP_TEST:
                        group_test_id = msg.detail['group_test_id']

                        self.room = Room_GroupTest(group_test_id)  # create the room

                        if self.room.authenticate(msg.detail['password']) is False:  # false password
                            await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('Group test password is wrong').serialize())
                            continue

                        if self.room_manager.get_room(group_test_id) is None:  # room not exist in room manager
                            if self.room.is_exist() is False:  # check if group test is exist
                                await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test not found').serialize())
                                continue

                            if self.room.is_active() is False:  # check if group test is active
                                await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test is not active').serialize())
                                continue

                            if self.room.check_student_in_group(self.student.id) is False:  # student not in group
                                await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('You are not in this group').serialize())
                                continue

                            print(f'Room {group_test_id} created by first student {self.student.id}')
                            self.room_manager.add_room(group_test_id, self.room)  # add room to manager

                        else:  # room exist in room manager
                            self.room = self.room_manager.get_room(group_test_id)  # get room from manager

                            # check if student has already joined this room
                            if self.room.check_student_join(self.student.id):
                                await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('You have already joined this room').serialize())
                                self.grouptest_student = self.room.get_grouptest_student(self.student.id)  # get before grouptest_student from room
                                continue
                            if self.room.check_student_in_group(self.student.id) is False:  # student not in group. just in case. may be redundant
                                await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('You are not in this group').serialize())
                                continue

                        self.room.add_grouptest_student(self.grouptest_student)  # add student to room
                        self.grouptest_student.set_room(self.room)  # set room to student

                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Joined successfully').serialize())
                        continue

                    if self.grouptest_student.get_room() is None:  # check if student has joined any group
                        await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message('You have not joined any group').serialize())
                        continue

                    # COMMAND: GET TEST
                    if msg.command == ClientMessage.GET_TEST:  # get test
                        if self.student_test is None:
                            self.student_test = self.room.get_student_test(self.student.id)
                            if self.student_test is None:
                                self.student_test = self.room.generate_student_test(self.student.id)

                        if self.student_test.is_submitted():
                            await self.websocket.send_json(self.response.set_status(status.HTTP_400_BAD_REQUEST).set_message('You have submitted').serialize())
                            break

                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message(self.grouptest_student.serialize(include={'violate', 'score', 'student_test', 'time_remaining'})).serialize())
                        self.room.set_state(self.student.id, GroupTest_Student.STATE_WORKING)
                        await self.room.notify_student_information(self.student.id)
                        continue

                    if self.student_test is None:
                        await self.websocket.send_json(self.response.set_status(status.HTTP_400_BAD_REQUEST).set_message('You have not get test yet').serialize())
                        continue

                    # COMMAND: UPDATE ANSWER
                    if msg.command == ClientMessage.ANSWER:
                        index: int = msg.detail['index']
                        answer: list[int] = msg.detail['answer']
                        self.student_test.student_work[index].student_answer = answer
                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Updated').serialize())
                        continue

                    # COMMAND: VIOLATE
                    if msg.command == ClientMessage.VIOLATE:
                        self.room.increase_violate(self.student.id)
                        if 0 < self.room.get_max_violate() <= self.student_test.violate:
                            # await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('You have violated the limit more times than allowed. The system will automatically submit.').serialize())
                            msg.command = ClientMessage.SUBMIT_TEST
                        else:
                            await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message({'violate': self.grouptest_student.get_violate()}).serialize())
                            await self.room.notify_student_information(self.student.id)
                            continue

                    # COMMAND: SUBMIT TEST
                    if msg.command == ClientMessage.SUBMIT_TEST:
                        try:
                            self.room.submit(self.student.id)
                            await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message({'score': self.grouptest_student.get_score()}).serialize())
                            self.room.set_state(self.student.id, GroupTest_Student.STATE_SUBMIT)
                            await self.room.notify_student_information(self.student.id)
                        except Exception as e:
                            pass
                        await self.websocket.close()
                        raise WebSocketDisconnect()

                except WebSocketDisconnect:
                    if self.grouptest_student.get_room() is not None:
                        self.grouptest_student.get_room().student_leave(self.student.id)
                    self.room_manager.remove_room(self.grouptest_student.get_room())
                    raise
                except Exception as e:
                    continue

        except WebSocketDisconnect:
            pass
