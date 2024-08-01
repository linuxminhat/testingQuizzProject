import random
from collections import defaultdict
from datetime import datetime

from Backend.Business import bcrypt_context
from Backend.Model.DB_model import StudentTest, GroupTest, Test, Question, StudentWork_Question
from Backend.WebSocket.Business.BO_Room_GroupTest import BO_Room_GroupTest
from Backend.WebSocket.Entity.GroupTest_Student import GroupTest_Student
from Backend.WebSocket.Entity.GroupTest_Teacher import GroupTest_Teacher


class Room_GroupTest:  # Room of group test. Contain all student and teacher in group test.
    def __init__(self, group_test_id: str):
        self.group_test_id = group_test_id
        self.teacher: GroupTest_Teacher = None
        self.students: dict[str, GroupTest_Student] = dict()
        self.submit_count = 0
        self._group_test: GroupTest = None
        self._test: Test = None
        self._questions: defaultdict[int, list[Question]] = None
        self._bo_room_grouptest = None

    @property
    def bo_room_grouptest(self):
        if self._bo_room_grouptest is None:
            self._bo_room_grouptest = BO_Room_GroupTest()
        return self._bo_room_grouptest

    @property
    def group_test(self) -> GroupTest:
        if self._group_test is None:
            self._group_test = self.bo_room_grouptest.get_group_test_by_id(self.group_test_id)
        return self._group_test

    @property
    def hash_pswd(self):
        return self.group_test.hash_pswd

    @hash_pswd.setter
    def hash_pswd(self, value):
        self.group_test.hash_pswd = value

    @property
    def questions(self):
        if self._questions is None:
            questions = self.bo_room_grouptest.get_all_questions_in_test(self.group_test.test_id)
            self._questions = defaultdict(list)
            for q in questions:
                self._questions[q.difficulty].append(q)
        return self._questions

    @property
    def test(self):
        if self._test is None:
            self._test = self.bo_room_grouptest.get_test_by_id(self.group_test.test_id)
        return self._test

    def add_grouptest_student(self, grouptest_student: GroupTest_Student):
        self.students[grouptest_student.get_student().id] = grouptest_student

    def get_grouptest_student(self, student_id: str) -> GroupTest_Student:
        return self.students[student_id]

    def get_student_test(self, student_id: str) -> StudentTest:
        if student_id in self.students.keys():  # check if student is in room
            grouptest_student = self.students[student_id]
            student_test = grouptest_student.get_student_test()
            if student_test is None:
                student_test = self.bo_room_grouptest.get_student_test(self.group_test_id, student_id)  # get student test from db
                if student_test is not None:
                    grouptest_student.set_student_test(student_test)
                    grouptest_student.get_test_timestamp = datetime.now()
                    grouptest_student.time_remaining = self.group_test.duration * 60  # convert minute to second. because just get from db so time remaining is full

            return student_test
        return None

    def generate_student_work_question(self) -> list[StudentWork_Question]:
        stw = list()
        for ts in self.test.structure:
            for noq in ts.number_of_question:
                num_question = min(noq.number_of_question, len(self.questions[noq.difficulty]))
                if self.group_test.shuffle:
                    for q in random.sample(self.questions[noq.difficulty], num_question):
                        stw.append(StudentWork_Question(content=q.content, answer=q.answer, attachment=q.attachment, student_answer=[]))
                else:
                    for q in self.questions[noq.difficulty][:num_question]:
                        stw.append(StudentWork_Question(content=q.content, answer=q.answer, attachment=q.attachment, student_answer=[]))
        return stw

    def generate_student_test(self, student_id: str) -> StudentTest:
        student_test = self.bo_room_grouptest.get_student_test(self.group_test_id, student_id)  # get student test from db
        if student_test is not None:
            self.students[student_id].set_student_test(student_test)
            return student_test
        # student test not exist
        # generate student work
        student_test = StudentTest(student_id=student_id, group_test_id=self.group_test_id, student_work=self.generate_student_work_question(), score=0, violate=0)
        self.bo_room_grouptest.insert_student_test(student_test)
        grouptest_student = self.students[student_id]
        grouptest_student.set_student_test(student_test)
        grouptest_student.get_test_timestamp = datetime.now()
        grouptest_student.time_remaining = self.group_test.duration * 60
        return student_test

    def is_active(self):
        return self.is_exist() and self.group_test.is_active()

    def is_exist(self):
        return self.group_test is not None

    def authenticate(self, password: str):
        return bcrypt_context.verify(password, self.hash_pswd)

    def check_student_in_group(self, student_id: str):
        return self.bo_room_grouptest.check_student_in_group(self.group_test.group_id, student_id)

    def check_owner(self, teacher_id: str):
        return self.bo_room_grouptest.check_owner(self.group_test.group_id, teacher_id)

    def check_student_join(self, student_id: str):
        return self.students.get(student_id, None) is not None

    def check_teacher_join(self):
        return self.teacher is not None

    def add_grouptest_teacher(self, grouptest_teacher: GroupTest_Teacher):
        self.teacher = grouptest_teacher

    def get_grouptest_teacher(self):
        return self.teacher

    def get_max_violate(self):
        return self.group_test.tolerance

    def get_student_information(self, student_id: str):
        if self.students[student_id]:
            return self.students[student_id].serialize(include={'student', 'state', 'violate', 'score'})
        return None

    def submit(self, student_id: str):
        self.bo_room_grouptest.submit(self.students[student_id].get_student_test())
        self.submit_count += 1

    def increase_violate(self, student_id: str):
        self.students[student_id].increase_violate()

    async def notify_student_information(self, student_id: str):
        if self.teacher is not None:
            await self.teacher.websocket.send_json(self.get_student_information(student_id))

    def set_state(self, student_id, state):
        self.students[student_id].set_state(state)

    def able_to_be_destroyed(self):
        if self.submit_count == len(self.students) and self.teacher is None:  # all student submitted and teacher left
            return True
        return False

    def teacher_leave(self):
        self.teacher = None

    def student_leave(self, student_id: str):
        self.students[student_id].update_time_remaining()