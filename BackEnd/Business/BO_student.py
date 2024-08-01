import asyncio
import os
from fastapi import UploadFile
from Backend.Model.DB_model import Student
from Backend.Model.request_model import Req_Student
from Backend.DataAccess.DAO_student import DAO_student
from Backend.Business import bcrypt_context, IMAGE_EXTENSIONS, save_file, STATIC_PATH


class BO_student:
    def __init__(self):
        self._dao_student = None

    @property
    def dao_student(self) -> DAO_student:
        if self._dao_student is None:
            self._dao_student = DAO_student()
        return self._dao_student

    # SELECT
    def authenticate(self, username: str, password: str) -> Student:
        student = self.dao_student.get_student_by_email(email=username)
        if student:
            if bcrypt_context.verify(secret=password, hash=student.hash_pswd):
                return student
        return None

    def get_student_by_id(self, student_id: str) -> Student:
        return self.dao_student.get_student_by_id(student_id)

    # INSERT
    def sign_up(self, data: Req_Student) -> str:
        if data.email is None:
            raise ValueError("Email is required!")
        if data.password is None:
            raise ValueError("Password is required!")

        return self.dao_student.insert_student(data.to_DB_model())

    # UPDATE
    def update_student(self, data: Req_Student):
        self.dao_student.update_student(data.to_DB_model())

    def update_is_banned(self, student_id: str, is_banned: bool) -> None:
        self.dao_student.update_is_banned(student_id=student_id, is_banned=is_banned)

    def update_is_verified(self, student_id: str, is_verified: bool) -> None:
        self.dao_student.update_is_verified(student_id=student_id, is_verified=is_verified)

    async def update_avatar(self, student_id: str, image: UploadFile) -> None:
        _, extension = os.path.splitext(image.filename)
        if extension.lower() not in IMAGE_EXTENSIONS:
            raise ValueError("Not supported extension: " + str(IMAGE_EXTENSIONS))
        relative_path = os.path.join("Student", student_id, "Avatar", student_id + extension)
        abs_path = os.path.join(STATIC_PATH, relative_path)
        await asyncio.gather(self.upload_avatar_path(student_id=student_id, avatar_path=relative_path),
                             save_file(path=abs_path, file=image))
        return relative_path

    async def upload_avatar_path(self, student_id: str, avatar_path: str):
        self.dao_student.update_avatar_path(student_id=student_id, avatar_path=avatar_path)
