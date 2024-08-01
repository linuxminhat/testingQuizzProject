from fastapi import WebSocket
from starlette import status
from starlette.websockets import WebSocketDisconnect

from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_teacher import BO_teacher
from Backend.Model.DB_model import Teacher
from Backend.WebSocket.Business.Room_Manager import Room_Manager
from Backend.WebSocket.Entity.ClientMessage import ClientMessage
from Backend.WebSocket.Entity.GroupTest_Teacher import GroupTest_Teacher
from Backend.WebSocket.Entity.ResponseMessage import ResponseMessage
from Backend.WebSocket.Entity.Room_GroupTest import Room_GroupTest


class BO_Teacher_Message:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.teacher = None
        self.room = None
        self.room_manager = None
        self.message = None
        self.response = None
        self.grouptest_teacher = None

    async def handle(self):
        try:
            await self.websocket.accept()
            self.room_manager = Room_Manager()
            self.message = ClientMessage()
            self.response = ResponseMessage()
            self.grouptest_teacher = GroupTest_Teacher(self.websocket)


            while True:
                try:
                    msg = self.message.set_message(**await self.websocket.receive_json())
                    if msg.command == ClientMessage.AUTHENTICATE:
                        self.teacher = await get_current_user(msg.detail['token'])
                        self.teacher = BO_teacher().get_teacher_by_id(self.teacher.id)
                        if self.teacher is None or not isinstance(self.teacher, Teacher):
                            self.teacher = None
                            await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('Invalid token').serialize())
                            continue

                        self.grouptest_teacher.set_teacher(self.teacher)
                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Authenticated').serialize())
                        continue

                    if self.teacher is None:  # check if teacher is authenticated
                        await self.websocket.send_json(self.response.set_status(status.HTTP_401_UNAUTHORIZED).set_message('You have not authenticated').serialize())
                        continue  # if not, continue to next loop

                    if msg.command == ClientMessage.JOIN_GROUP_TEST:
                        group_test_id = msg.detail['group_test_id']

                        self.room = Room_GroupTest(group_test_id)  # create the room

                        if self.room_manager.get_room(group_test_id) is None:  # room not exist in room manager
                            if self.room.is_exist() is False:  # check if group test is exist
                                await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test not found').serialize())
                                continue

                            if self.room.is_active() is False:  # check if group test is active
                                await self.websocket.send_json(self.response.set_status(status.HTTP_404_NOT_FOUND).set_message('Group test is not active').serialize())
                                continue

                            if self.room.check_owner(self.teacher.id) is False:  # teacher not own group
                                await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message(f'You not own this group').serialize())
                                continue

                            print(f'Room {group_test_id} created by teacher {self.teacher.id}')
                            self.room_manager.add_room(group_test_id, self.room)  # add room to manager

                        else:  # room exist in room manager
                            self.room = self.room_manager.get_room(group_test_id)  # get room from manager
                            if self.room.check_owner(self.teacher.id) is False:  # teacher not own group
                                await self.websocket.send_json(self.response.set_status(status.HTTP_403_FORBIDDEN).set_message(f'You not own this group').serialize())
                                continue

                        self.room.add_grouptest_teacher(self.grouptest_teacher)  # add teacher to room
                        self.grouptest_teacher.set_room(self.room)  # set room to teacher

                        await self.websocket.send_json(self.response.set_status(status.HTTP_200_OK).set_message('Joined successfully').serialize())
                        continue

                except WebSocketDisconnect:
                    self.room.teacher_leave()
                    self.room_manager.remove_room(self.grouptest_teacher.get_room())
                    raise
                except Exception as e:
                    continue

        except WebSocketDisconnect:
            pass
