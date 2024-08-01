from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.DataAccess.DAO_test import DAO_test
from Backend.DataAccess.DAO_test_structure import DAO_test_structure
from Backend.Model.DB_model import TestStructure, Test
from Backend.Model.request_model import Req_Test


class BO_test:
    def __init__(self):
        self._dao_test = None
        self._dao_collection = None
        self._dao_test_structure = None

    @property
    def dao_test(self) -> DAO_test:
        if self._dao_test is None:
            self._dao_test = DAO_test()
        return self._dao_test

    @property
    def dao_collection(self) -> DAO_collection:
        if self._dao_collection is None:
            self._dao_collection = DAO_collection()
        return self._dao_collection

    @property
    def dao_test_structure(self) -> DAO_test_structure:
        if self._dao_test_structure is None:
            self._dao_test_structure = DAO_test_structure()
        return self._dao_test_structure

    # SELECT
    def get_test_by_collection(self, collection_id: str, teacher_id=None):
        if teacher_id is not None and self.dao_collection.check_owner(collection_id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the collection {collection_id}!")

        for test in self.dao_test.get_test_by_collection(collection_id):
            test.structure = self.dao_test_structure.get_structure(test.id)
            yield test

    def get_test_by_id(self, test_id: str) -> Test:
        test = self.dao_test.get_test_by_id(test_id)
        test.structure = self.dao_test_structure.get_structure(test_id)
        return test

    # INSERT
    def insert_test(self, teacher_id: str, data: Req_Test) -> str:
        if self.dao_collection.check_owner(data.collection_id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the collection {data.collection_id}!")

        test_id = self.dao_test.insert_test(data.to_DB_model())

        return test_id

    # UPDATE
    def update_test(self, teacher_id, data: Req_Test):
        if self.dao_test.check_owner(data.id, teacher_id) is False:
            raise ValueError(f"The teacher {teacher_id} is not the owner of the test {data.id}!")

        self.dao_test.update_test(data.to_DB_model())
