import asyncio
import os.path

from fastapi import UploadFile
from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_Teacher
from Backend.DataAccess.DAO_teacher import DAO_teacher
from Backend.Business import bcrypt_context, STATIC_PATH, save_file, IMAGE_EXTENSIONS


class BO_teacher:
    def __init__(self):
        self._dao_teacher = None

    @property
    def dao_teacher(self) -> DAO_teacher:
        if self._dao_teacher is None:
            self._dao_teacher = DAO_teacher()
        return self._dao_teacher

    # SELECT
    def authenticate(self, username: str, password: str) -> Teacher | None:
        teacher = self.dao_teacher.get_teacher_by_email(email=username)
        if teacher:
            if bcrypt_context.verify(secret=password, hash=teacher.hash_pswd):
                return teacher
        return None

    def get_teacher_by_id(self, teacher_id: str) -> Teacher:
        return self.dao_teacher.get_teacher_by_id(teacher_id)

    # INSERT
    def sign_up(self, data: Req_Teacher) -> str:
        if data.email is None:
            raise ValueError("Email is required!")
        if data.password is None:
            raise ValueError("Password is required!")
        if data.name is None:
            raise ValueError("Name is required!")

        return self.dao_teacher.insert_teacher(data.to_DB_model())

    # UPDATE
    def update_teacher(self, data: Req_Teacher) -> None:
        if data.id is None:
            raise ValueError("Teacher ID is required!")

        self.dao_teacher.update_teacher(data.to_DB_model())

    def update_password(self, teacher_id: str, password: str) -> None:
        self.dao_teacher.update_password(teacher_id=teacher_id, hash_pswd=bcrypt_context.hash(password))

    def update_name(self, teacher_id: str, name: str) -> None:
        self.dao_teacher.update_name(teacher_id=teacher_id, name=name)

    def update_is_banned(self, teacher_id: str, is_banned: bool) -> None:
        self.dao_teacher.update_is_banned(teacher_id=teacher_id, is_banned=is_banned)

    def update_is_verified(self, teacher_id: str, is_verified: bool) -> None:
        self.dao_teacher.update_is_verified(teacher_id=teacher_id, is_verified=is_verified)

    async def update_avatar(self, teacher_id: str, image: UploadFile) -> None:
        _, extension = os.path.splitext(image.filename)
        if extension.lower() not in IMAGE_EXTENSIONS:
            raise ValueError("Not supported extension: " + str(IMAGE_EXTENSIONS))
        relative_path = os.path.join("Teacher", teacher_id, "Avatar", teacher_id + extension)
        abs_path = os.path.join(STATIC_PATH, relative_path)
        await asyncio.gather(self.upload_avatar_path(teacher_id=teacher_id, avatar_path=relative_path),
                             save_file(path=abs_path, file=image))
        return relative_path

    async def upload_avatar_path(self, teacher_id: str, avatar_path: str):
        self.dao_teacher.update_avatar_path(teacher_id=teacher_id, avatar_path=avatar_path)
