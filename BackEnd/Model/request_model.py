import pickle
from pydantic import BaseModel, EmailStr, Field, conlist

from Backend.Business import bcrypt_context
from Backend.Model.DB_model import *


class Req_Admin(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    username: str = Field(None, max_length=255)
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False

    def to_DB_model(self) -> Admin:
        admin = Admin(self.model_dump(exclude={'password'}))
        if self.password is not None:
            admin.hash_pswd = bcrypt_context.hash(self.password)
        return admin


class Req_Teacher(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    email: EmailStr = None
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False
    is_verified: bool = False

    def to_DB_model(self) -> Teacher:
        teacher = Teacher(self.model_dump(exclude={'password'}))
        if self.password is not None:
            teacher.hash_pswd = bcrypt_context.hash(self.password)
        return teacher


class Req_Student(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    email: EmailStr = None
    password: str = Field(None, min_length=8, max_length=64)
    name: str = Field(None, max_length=100)
    is_banned: bool = False
    is_verified: bool = False

    def to_DB_model(self) -> Student:
        student = Student(self.model_dump(exclude={'password'}))
        if self.password is not None:
            student.hash_pswd = bcrypt_context.hash(self.password)
        return student


class Req_Group(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)
    teacher_id: str = Field(None, min_length=8, max_length=8)
    is_show: bool = True
    image_path: str = None

    def to_DB_model(self) -> Group:
        return Group(self.model_dump())


class Req_GroupStudent(BaseModel):
    group_id: str = Field(None, min_length=8, max_length=8)
    student_id: str = Field(None, min_length=8, max_length=8)
    is_join: bool = True
    is_show: bool = True

    class Req_InsertedInformation(BaseModel):
        student_id: conlist(str, min_length=1, max_length=8) = None
        student_email: list[EmailStr] = None

    def to_DB_model(self) -> GroupStudent:
        return GroupStudent(self.model_dump())


class Req_Collection(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    teacher_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)

    def to_DB_model(self) -> Collection:
        return Collection(self.model_dump())


class Req_QuestionBank(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    collection_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)

    def to_DB_model(self) -> QuestionBank:
        return QuestionBank(self.model_dump())


class Req_NumberOfQuestion(BaseModel):
    difficulty: int = Field(ge=1, le=5)
    number_of_question: int = Field(ge=1)

    def to_DB_model(self) -> NumberOfQuestion:
        return NumberOfQuestion(self.model_dump())


class Req_TestStructure(BaseModel):
    test_id: str = Field(None, min_length=8, max_length=8)
    question_bank_id: str = Field(min_length=8, max_length=8)
    number_of_question: list[Req_NumberOfQuestion]

    def to_DB_model(self) -> TestStructure:
        return TestStructure(self.model_dump(exclude={'number_of_question'}), number_of_question=[noq.to_DB_model() for noq in self.number_of_question])


class Req_Test(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    collection_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)
    structure: list[Req_TestStructure]

    def to_DB_model(self) -> Test:
        return Test(self.model_dump(exclude={'structure'}), structure=[structure.to_DB_model() for structure in self.structure])


class Req_Answer(BaseModel):
    text: list[str] = list[Field(max_length=256)]
    correct: set[int] = set[Field(0, ge=0)]

    def to_DB_model(self) -> Answer:
        return Answer(self.model_dump())


class Req_Question(BaseModel):
    id: str = Field(None, min_length=10, max_length=10)
    question_bank_id: str = Field(None, min_length=8, max_length=8)
    content: str = Field(None, max_length=512)
    answer: Req_Answer = None
    difficulty: int = Field(None, ge=1, le=5)

    def to_DB_model(self) -> Question:
        return Question(self.model_dump(exclude={'answer'}), answer=self.answer.to_DB_model())


class Req_GroupTest(BaseModel):
    id: str = Field(None, min_length=8, max_length=8)
    group_id: str = Field(None, min_length=8, max_length=8)
    test_id: str = Field(None, min_length=8, max_length=8)
    name: str = Field(None, max_length=100)
    password: str = Field(None, max_length=64)
    start: datetime = None
    end: datetime = None
    duration: int = Field(None, ge=1, le=180)
    shuffle: bool = None
    tolerance: int = Field(None, ge=0, le=255)
    n_page: int = Field(1, ge=1, le=255)
    allow_move: bool = True

    def to_DB_model(self) -> GroupTest:
        group_test = GroupTest(self.model_dump(exclude={'passsword'}))
        if self.password is not None:
            group_test.hash_pswd = bcrypt_context.hash(self.password)
        return group_test


class Req_StudentWork(BaseModel):
    group_test_id: str = Field(min_length=8, max_length=8)
    student_answer: list[list[int]] = list[list[Field(None, ge=0)]]


class Req_StudentTest(BaseModel):
    student_id: str = Field(None, min_length=8, max_length=8)
    group_test_id: str = Field(min_length=8, max_length=8)

    def to_DB_model(self) -> StudentTest:
        return StudentTest(self.model_dump())
