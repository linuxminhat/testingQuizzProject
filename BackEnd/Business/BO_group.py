import os
import random

from Backend.Business import STATIC_PATH
from Backend.DataAccess.DAO_group import DAO_group
from Backend.Model.DB_model import Group
from Backend.Model.request_model import Req_Group


class BO_group:
    def __init__(self):
        self._dao_group = None

    @property
    def dao_group(self) -> DAO_group:
        if self._dao_group is None:
            self._dao_group = DAO_group()
        return self._dao_group

    # SELECT
    def get_groups_by_teacher(self, teacher_id: str, is_show: bool = True) -> list[Group]:
        return self.dao_group.get_groups_by_teacher(teacher_id=teacher_id, is_show=is_show)

    def get_group_by_id(self, teacher_id: str, group_id: str) -> Group:
        group = self.dao_group.get_group_by_id(group_id)
        if group.teacher_id != teacher_id:
            raise Exception(f"Group {group_id} is not belong to teacher {teacher_id}!")
        return group

    def check_owner(self, group_id: str, teacher_id: str) -> bool:
        return self.dao_group.check_owner(group_id, teacher_id)

    # INSERT
    def insert_group(self, data: Req_Group) -> str:
        if data.teacher_id is None:
            raise Exception("teacher_id is required!")
        group = data.to_DB_model()
        group.image_path = os.path.join('Group', 'Images', random.choice(os.listdir(os.path.join(STATIC_PATH, 'Group', 'Images'))))
        return self.dao_group.insert_group(group)

    # UPDATE
    def update_group(self, data: Req_Group):
        group = data.to_DB_model()
        if group.id is None:
            raise Exception("id is required!")
        if group.teacher_id is None:
            raise Exception("teacher_id is required!")

        self.dao_group.update_group(group)
