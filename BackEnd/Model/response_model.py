from pydantic import BaseModel
from Backend.Model.DB_model import *


class Res_Token(BaseModel):
    access_token: str
    token_type: str


class Res_Student(BaseModel):
    id: str | None
    email: str | None
    name: str | None
    avatar_path: str | None
    is_banned: bool | None
    created_timestamp: datetime | None
    is_verified: bool | None

    @classmethod
    def from_DB_model(cls, student: Student):
        return cls(**student.jsonify()) if student else None


class Res_Teacher(BaseModel):
    id: str
    email: str
    name: str | None = None
    avatar_path: str | None = None
    is_banned: bool | None = None
    created_timestamp: datetime | None = None
    is_verified: bool | None = None

    @classmethod
    def from_DB_model(cls, teacher: Teacher):
        return cls(**teacher.jsonify()) if teacher else None


class Res_Group(BaseModel):
    id: str
    name: str | None = None
    teacher_id: str | None = None
    created_timestamp: datetime | None = None
    is_show: bool | None = None
    image_path: str | None = None

    @classmethod
    def from_DB_model(cls, group: Group):
        return cls(**group.jsonify()) if group else None


class Res_GroupStudent(BaseModel):
    group_id: str
    student_id: str
    is_join: bool | None = None
    request_timestamp: datetime | None = None
    is_show: bool | None = None


class Res_Collection(BaseModel):
    id: str
    teacher_id: str
    name: str | None = None
    created_timestamp: datetime | None

    @classmethod
    def from_DB_model(cls, collection: Collection):
        return cls(**collection.jsonify()) if collection else None


class Res_QuestionBank(BaseModel):
    id: str
    collection_id: str | None = None
    name: str | None = None
    created_timestamp: datetime | None = None

    @classmethod
    def from_DB_model(cls, question_bank: QuestionBank):
        return cls(**question_bank.jsonify()) if question_bank else None


class Res_GroupTest(BaseModel):
    id: str | None = None
    group_id: str | None = None
    test_id: str | None = None
    name: str | None = None
    start: datetime | None = None
    end: datetime | None = None
    duration: int | None = None
    shuffle: bool | None = None
    tolerance: int | None = None
    created_timestamp: datetime | None = None
    n_page: int | None = None
    allow_move: bool | None = None

    @classmethod
    def from_DB_model(cls, group_test: GroupTest):
        return cls(**group_test.jsonify()) if group_test else None


class Res_Answer(BaseModel):
    text: list[str]
    correct: set[int]

    @classmethod
    def from_DB_model(cls, answer: Answer):
        return cls(text=answer.text, correct=answer.correct)


class Res_Question(BaseModel):
    id: str | None = None
    question_bank_id: str | None = None
    order_number: int | None = None
    content: str | None = None
    answer: Res_Answer | None = None
    attachment: list[str] | None = None
    difficulty: int | None = None

    @classmethod
    def from_DB_model(cls, question: Question):
        return cls(id=question.id, question_bank_id=question.question_bank_id, order_number=question.order_number,
                   content=question.content, answer=Res_Answer.from_DB_model(question.answer),
                   attachment=question.attachment,
                   difficulty=question.difficulty) if question else None


class Res_NumberOfQuestion(BaseModel):
    difficulty: int
    number_of_question: int

    @classmethod
    def from_DB_model(cls, number_of_question: NumberOfQuestion):
        return cls(**number_of_question.jsonify()) if number_of_question else None


class Res_TestStructure(BaseModel):
    test_id: str | None = None
    question_bank_id: str
    number_of_question: list[Res_NumberOfQuestion] | None = None

    @classmethod
    def from_DB_model(cls, test_structure: TestStructure):
        return cls(test_id=test_structure.test_id, question_bank_id=test_structure.question_bank_id,
                   number_of_question=[Res_NumberOfQuestion.from_DB_model(number_of_question) for number_of_question in
                                       test_structure.number_of_question]) if test_structure else None


class Res_Test(BaseModel):
    id: str
    collection_id: str
    name: str
    created_timestamp: datetime
    structure: list[Res_TestStructure] | None = None

    @classmethod
    def from_DB_model(cls, test: Test):
        return cls(id=test.id,
                   collection_id=test.collection_id,
                   name=test.name,
                   created_timestamp=test.created_timestamp,
                   structure=[Res_TestStructure.from_DB_model(structure) for structure in test.structure] if test.structure else None) if test else None


class Res_StudentWork_Question(BaseModel):
    content: str | None = None
    answer: Res_Answer | None = None
    attachment: list[str] | None = None
    student_answer: list[int] | None = None

    @classmethod
    def from_DB_model(cls, student_work_question: StudentWork_Question):
        return cls(content=student_work_question.content,
                   answer=Res_Answer.from_DB_model(student_work_question.answer),
                   attachment=student_work_question.attachment,
                   student_answer=student_work_question.student_answer)


class Res_StudentTest(BaseModel):
    student_id: str | None = None
    group_test_id: str | None = None
    start: datetime | None = None
    end: datetime | None = None
    student_work: list[Res_StudentWork_Question] | None = None
    score: float | None = None
    violate: int | None = None
    student: Res_Student | None = None
    group_test: Res_GroupTest | None = None

    @classmethod
    def from_DB_model(cls, student_test: StudentTest):
        return cls(student_id=student_test.student_id
                   , group_test_id=student_test.group_test_id
                   , start=student_test.start
                   , end=student_test.end
                   , student_work=[Res_StudentWork_Question.from_DB_model(sw) for sw in student_test.student_work] if student_test.student_work else None
                   , score=student_test.score
                   , violate=student_test.violate
                   , student=Res_Student.from_DB_model(student_test.student) if student_test.student else None
                   , group_test=Res_GroupTest.from_DB_model(student_test.group_test) if student_test.group_test else None) if student_test else None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class Res_StudentScore(BaseModel):
    student_id: str | None = None
    name: str | None = None
    avatar_path: str | None = None
    point: float | None = None
