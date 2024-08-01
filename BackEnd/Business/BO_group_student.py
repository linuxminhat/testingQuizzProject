from Backend.DataAccess.DAO_group import DAO_group
from Backend.DataAccess.DAO_group_student import DAO_group_student
from Backend.DataAccess.DAO_student import DAO_student
from Backend.Model.DB_model import Group, Student
from Backend.Model.request_model import Req_GroupStudent


class BO_group_student:
    def __init__(self):
        self._dao_group_student = None
        self._dao_group = None
        self._dao_student = None

    @property
    def dao_group_student(self):
        if self._dao_group_student is None:
            self._dao_group_student = DAO_group_student()
        return self._dao_group_student

    @property
    def dao_group(self):
        if self._dao_group is None:
            self._dao_group = DAO_group()
        return self._dao_group

    @property
    def dao_student(self):
        if self._dao_student is None:
            self._dao_student = DAO_student()
        return self._dao_student

    # SELECT
    def get_group_id_by_student(self, student_id: str, is_join: bool = True) -> list[str]:
        return self.dao_group_student.get_group_id_by_student(student_id=student_id, is_join=is_join)

    def get_groups_by_student(self, student_id: str, is_join: bool = True) -> list[Group]:
        return self.dao_group_student.get_groups_by_student(student_id=student_id, is_join=is_join)

    def get_students_by_group(self, teacher_id: str, group_id: str, is_join: bool = True) -> list[Student]:
        if self.dao_group.check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")

        return self.dao_group_student.get_students_by_group(group_id=group_id, is_join=is_join)

    def get_other_students_by_group(self, student_id: str, group_id: str) -> list[Student]:
        if self.check_student_in_group(group_id, student_id) is False:
            raise ValueError(f"student {student_id} is not in group {group_id}")

        return self.dao_group_student.get_students_by_group(group_id=group_id, is_join=True)

    def check_student_in_group(self, group_id: str, student_id: str) -> bool:
        return self.dao_group_student.check_student_in_group(group_id, student_id)

    # INSERT
    def request_join(self, group_id: str, student_id: str) -> None:
        if group_id is None:
            raise ValueError("group_id is required!")
        if student_id is None:
            raise ValueError("student_id is required!")

        self.dao_group_student.request_join(group_id=group_id, student_id=student_id)

    def insert_students(self, teacher_id: str, group_id: str, data: Req_GroupStudent.Req_InsertedInformation):
        if teacher_id is not None and self.dao_group.check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to teacher {teacher_id}")
        if data.student_id is not None and len(data.student_id) != 0:
            self.dao_group_student.insert_students_by_id(group_id=group_id, list_id=data.student_id)
        if data.student_email is not None and len(data.student_email) != 0:
            list_id = self.dao_student.get_student_list_id_by_list_email(data.student_email)
            self.dao_group_student.insert_students_by_id(group_id=group_id, list_id=list_id)

    def update_student_group(self, data: Req_GroupStudent):
        if data.student_id is None:
            raise ValueError("student_id is required!")
        if data.group_id is None:
            raise ValueError("group_id is required!")
        self.dao_group_student.update(data.to_DB_model())

    def delete_students(self, teacher_id: str, group_id: str, list_id: list[str]) -> None:
        if teacher_id is not None and self.dao_group.check_owner(group_id, teacher_id) is False:
            raise ValueError(f"group {group_id} does not belong to {teacher_id}")

        if len(list_id) != 0:
            self.dao_group_student.delete_students_by_id(group_id=group_id, list_id=list_id)

    def leave_group(self, student_id: str, group_id: str):
        self.dao_group_student.delete_student(student_id=student_id, group_id=group_id)
