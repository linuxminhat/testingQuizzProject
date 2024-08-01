import os
import shutil
import asyncio
from fastapi import UploadFile
from Backend.Model.DB_model import Question, NumberOfQuestion
from Backend.Model.request_model import Req_Question
from Backend.DataAccess import generate_id
from Backend.DataAccess.DAO_question import DAO_question
from Backend.DataAccess.DAO_question_bank import DAO_question_bank
from Backend.Business import STATIC_PATH, save_file, ACCEPTED_FILE_EXTENSIONS


class BO_question:
    def __init__(self):
        self._dao_question = None
        self._dao_question_bank = None

    @property
    def dao_question_bank(self) -> DAO_question_bank:
        if self._dao_question_bank is None:
            self._dao_question_bank = DAO_question_bank()
        return self._dao_question_bank

    @property
    def dao_question(self) -> DAO_question:
        if self._dao_question is None:
            self._dao_question = DAO_question()
        return self._dao_question

    @staticmethod
    def get_from_attachment_path(attachment_path: str, component: str = 'question_id') -> str:
        components = attachment_path.split(os.sep)
        if component == 'question_id':
            return components[-2]

    # INSERT
    def insert_question(self, data: Req_Question) -> str:
        return self.dao_question.insert_question(data.to_DB_model())

    def insert_questions(self, teacher_id: str, question_bank_id: str, data: list[Req_Question]) -> list[str]:
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")

        if len(data) == 1:
            data[0].question_bank_id = question_bank_id
            return [self.insert_question(data[0])]
        return self.dao_question.insert_questions(question_bank_id, [q.to_DB_model() for q in data])

    async def insert_attachment(self, teacher_id: str, question_id: str, attachment: list[UploadFile]):
        if self.dao_question.check_owner(teacher_id=teacher_id, question_id=question_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question {question_id}!")

        # get question_bank information to get collection_id & question_bank_id
        question_bank = self.dao_question.get_question_bank(question_id)
        if question_bank is None:
            raise ValueError(f"Question {question_id} does not exist!")

        tasks = []
        attachment_path = []
        for file in attachment:
            _, extension = os.path.splitext(file.filename)
            if extension.lower() not in ACCEPTED_FILE_EXTENSIONS:
                raise ValueError(
                    f"Extension {extension} is not accepted! Only {ACCEPTED_FILE_EXTENSIONS} are accepted!")

            relative_path = os.path.join("Teacher", teacher_id, "Collection", question_bank.collection_id,
                                         "QuestionBank", question_bank.id, "Question", question_id,
                                         generate_id(5) + extension)
            abs_path = os.path.join(STATIC_PATH, relative_path)
            tasks.append(asyncio.create_task(save_file(path=abs_path, file=file)))
            attachment_path.append(relative_path)

        tasks.append(asyncio.create_task(self.dao_question.insert_attachment_path(question_id, attachment_path)))
        await asyncio.gather(*tasks)

        return attachment_path

    # SELECT
    def get_questions_in_bank(self, teacher_id: str, question_bank_id: str, offset: int, length: int) -> list[Question]:
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        return self.dao_question.get_questions_in_bank(question_bank_id, offset=offset, length=length)

    def summary(self, teacher_id: str, question_bank_id: str) -> list[NumberOfQuestion]:
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")
        return self.dao_question.summary(question_bank_id)

    # UPDATE
    def update_questions(self, teacher_id: str, question_bank_id: str, data: list[Req_Question]):
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")

        self.dao_question.update_questions(question_bank_id, [q.to_DB_model() for q in data])

    # DELETE
    def delete_questions(self, teacher_id: str, question_bank_id: str, question_ids: list[str]):
        if self.dao_question_bank.check_owner(teacher_id=teacher_id, question_bank_id=question_bank_id) is False:
            raise ValueError(f"Teacher {teacher_id} is not owner of question bank {question_bank_id}!")

        if len(question_ids) == 1:
            self.dao_question.delete_question(question_bank_id=question_bank_id, question_id=question_ids[0])
        else:
            self.dao_question.delete_questions(question_bank_id=question_bank_id, question_ids=question_ids)

    def delete_attachment(self, teacher_id: str, attachment_path: str):
        if teacher_id in attachment_path:
            abs_path = os.path.join(STATIC_PATH, attachment_path)
            if os.path.exists(abs_path):

                # get question_id from attachment_path to remove attachment_path from question
                question_id = BO_question.get_from_attachment_path(attachment_path, 'question_id')
                question = self.dao_question.get_question_by_id(question_id)
                question.attachment.remove(attachment_path)

                if len(question.attachment) == 0:
                    # remove folder if there no file
                    shutil.rmtree(os.path.dirname(abs_path))
                    question.attachment = None
                else:
                    # remove file
                    os.remove(abs_path)
                self.dao_question.update_question_attachment(question)
