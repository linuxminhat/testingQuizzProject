from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.DataAccess.DAO_question_bank import DAO_question_bank
from Backend.Model.DB_model import QuestionBank
from Backend.Model.request_model import Req_QuestionBank


class BO_question_bank:
    def __init__(self):
        self._dao_question_bank = None
        self._dao_collection = None

    @property
    def dao_question_bank(self) -> DAO_question_bank:
        if self._dao_question_bank is None:
            self._dao_question_bank = DAO_question_bank()
        return self._dao_question_bank

    @property
    def dao_collection(self) -> DAO_collection:
        if self._dao_collection is None:
            self._dao_collection = DAO_collection()
        return self._dao_collection

    # INSERT
    def insert_question_bank(self, teacher_id: str, data: Req_QuestionBank) -> str:
        if data.collection_id is None:
            raise Exception("collection_id is required")
        if self.dao_collection.check_owner(collection_id=data.collection_id, teacher_id=teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of collection {data.collection_id}")
        return self.dao_question_bank.insert_question_bank(data.to_DB_model())

    # SELECT
    def get_question_banks_by_collection(self, teacher_id: str, collection_id: str) -> list[QuestionBank]:
        if self.dao_collection.check_owner(collection_id, teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of collection {collection_id}")

        return self.dao_question_bank.get_question_banks_by_collection(collection_id)

    # UPDATE
    def update_question_bank(self, teacher_id: str, data: Req_QuestionBank):
        if self.dao_collection.check_owner(self.dao_question_bank.get_collection_id(data.id), teacher_id) is False:
            raise Exception(f"teacher {teacher_id} is not the owner of question bank {data.id}")

        self.dao_question_bank.update(data.to_DB_model())
