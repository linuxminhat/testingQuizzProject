from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_group_test import BO_group_test
from Backend.Business.BO_student_test import BO_student_test
from Backend.Business.BO_test import BO_test
from Backend.Model.DB_model import GroupTest, Question, StudentTest


class BO_Room_GroupTest:
    def __init__(self):
        self._bo_group_test = None
        self._bo_group = None
        self._bo_group_student = None
        self._bo_test = None
        self._bo_student_test = None

    @property
    def bo_group_test(self):
        if self._bo_group_test is None:
            self._bo_group_test = BO_group_test()
        return self._bo_group_test

    @property
    def bo_group(self):
        if self._bo_group is None:
            self._bo_group = BO_group()
        return self._bo_group

    @property
    def bo_group_student(self):
        if self._bo_group_student is None:
            self._bo_group_student = BO_group_student()
        return self._bo_group_student

    @property
    def bo_test(self):
        if self._bo_test is None:
            self._bo_test = BO_test()
        return self._bo_test

    @property
    def bo_student_test(self):
        if self._bo_student_test is None:
            self._bo_student_test = BO_student_test()
        return self._bo_student_test

    def insert_student_test(self, student_test: StudentTest):
        return self.bo_student_test.insert_student_test(student_test)

    def get_test_by_id(self, test_id: str):
        return self.bo_test.get_test_by_id(test_id)

    def get_student_test(self, group_test_id: str, student_id: str):
        return self.bo_student_test.get_student_test(group_test_id, student_id)

    def get_group_test_by_id(self, group_test_id: str) -> GroupTest:
        return self.bo_group_test.get_group_test_by_id(group_test_id)

    def check_student_in_group(self, group_id: str, student_id: str) -> bool:
        return self.bo_group_student.check_student_in_group(group_id, student_id)

    def check_owner(self, group_id: str, teacher_id: str) -> bool:
        return self.bo_group.check_owner(group_id, teacher_id)

    def get_group_test_by_group(self, group_id: str) -> list[GroupTest]:
        return self.bo_group_test.get_group_test_by_group(group_id)

    def get_all_questions_in_test(self, test_id: str) -> list[Question]:
        return self.bo_group_test.get_all_questions_in_test(test_id)

    def submit(self, student_test: StudentTest):
        self.bo_student_test.submit(student_test)

    def update_violate(self, group_test_id: str, student_id: str, violate):
        self.bo_student_test.update_violate(group_test_id, student_id, violate)