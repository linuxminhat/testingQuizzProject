from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from typing import Annotated

from Backend.Model.request_model import Req_Collection
from Backend.Model.response_model import Res_Collection
from Backend.Model.DB_model import Teacher
from Backend.Business.BO_collection import BO_collection
from Backend.Business.BO_authenticate import get_current_user
from Backend.Router.test_router import test_router
from Backend.Router.question_bank_router import question_bank_router

collection_router = APIRouter(prefix='/collection', tags=['collection'])
collection_router.include_router(question_bank_router)
collection_router.include_router(test_router)


@collection_router.get('/', status_code=status.HTTP_200_OK)
async def get_collections(teacher: Annotated[Teacher, Depends(get_current_user)],
                          collection_service: Annotated[BO_collection, Depends()]):
    try:
        return [Res_Collection.from_DB_model(collection) for collection in
                collection_service.get_collections_by_teacher(teacher.id)]
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can not get collections!")


@collection_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Collection, Body()],
                            collection_service: Annotated[BO_collection, Depends()]) -> str:
    if isinstance(teacher, Teacher) is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Teacher is not valid!")
    try:
        data.teacher_id = teacher.id
        return collection_service.insert_collection(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@collection_router.patch('/update', status_code=status.HTTP_200_OK)
async def update_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Collection, Body()],
                            collection_service: Annotated[BO_collection, Depends()]):
    try:
        data.teacher_id = teacher.id
        collection_service.update_collection(data=data)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
