from Backend.Model.DB_model import Collection
from Backend.DataAccess.DAO_collection import DAO_collection
from Backend.Model.request_model import Req_Collection


class BO_collection:
    def __init__(self):
        self._dao_collection = DAO_collection()

    @property
    def dao_collection(self) -> DAO_collection:
        if self._dao_collection is None:
            self._dao_collection = DAO_collection()
        return self._dao_collection

    # SELECT
    def get_collections_by_teacher(self, teacher_id: str) -> list[Collection]:
        return self.dao_collection.get_collections_by_teacher(teacher_id)

    def get_collection_by_id(self, collection_id: str, teacher_id: str = None) -> Collection:
        if teacher_id is not None:
            if self.dao_collection.check_owner(collection_id=collection_id, teacher_id=teacher_id) is False:
                raise Exception(f"Collection {collection_id} is not belong to teacher {teacher_id}!")

        return self.dao_collection.get_collection_by_id(collection_id)

    # INSERT
    def insert_collection(self, data: Req_Collection) -> str:
        return self.dao_collection.insert_collection(data.to_DB_model())

    # UPDATE
    def update_collection(self, data: Req_Collection):
        if data.teacher_id is None:
            raise Exception("teacher_id is required!")
        if data.id is None:
            raise Exception("collection_id is required!")

        if self.dao_collection.check_owner(collection_id=data.id, teacher_id=data.teacher_id) is False:
            raise Exception(f"Collection {data.id} is not belong to teacher {data.teacher_id}!")

        self.dao_collection.update_collection(data.to_DB_model())
