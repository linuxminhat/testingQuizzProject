from datetime import datetime
from fastapi import WebSocket
from Backend.Model.DB_model import StudentTest, Student


class GroupTest_Student:
    STATE_DISCONNECTED = 'DISCONNECTED'
    STATE_READY = 'READY'
    STATE_WORKING = 'WORKING'
    STATE_BANNED = 'BANNED'
    STATE_SUBMIT = 'SUBMIT'

    def __init__(self, websocket: WebSocket):
        self.websocket = websocket
        self.student: Student = None
        self.student_test: StudentTest = None
        self.room = None
        self.state = self.STATE_READY
        self.get_test_timestamp = None
        self.time_remaining = 0

    def set_room(self, room):  # room: Room_GroupTest
        self.room = room
        return self

    def get_room(self):  # -> Room_GroupTest
        return self.room

    def set_state(self, state: str):
        self.state = state
        return self

    def get_state(self) -> str:
        return self.state

    def increase_violate(self):
        self.student_test.violate += 1
        return self

    def get_violate(self):
        if self.student_test is None:
            return 0
        return self.student_test.violate

    def set_student(self, student):
        self.student = student
        return self

    def get_student(self):
        return self.student

    def get_student_test(self):
        return self.student_test

    def set_student_test(self, student_test: StudentTest):
        self.student_test = student_test
        return self

    def serialize(self, include: set):
        ser = {
            'student': self.student.serialize({'id', 'name', 'avatar_path'}) if 'student' in include else None,
            'violate': self.get_violate() if 'violate' in include else None,
            'state': self.state if 'state' in include else None,
            'score': self.student_test.score if 'score' in include and self.student_test is not None else 0,
            'student_test': self.student_test.serialize() if 'student_test' in include and self.student_test is not None else None,
            'time_remaining': self.time_remaining if 'time_remaining' in include else None
        }

        return {k: v for k, v in ser.items() if v is not None}

    def get_score(self):
        return self.student_test.score

    # def submit(self, student_answer: list[list[int]]):
    #     student_test = self.room.submit(self.student.id, student_answer)
    #     self.set_student_test(student_test)
    def update_time_remaining(self):
        self.time_remaining -= (datetime.now() - self.get_test_timestamp).total_seconds()
