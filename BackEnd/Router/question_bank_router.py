from fastapi import APIRouter, HTTPException, Depends, Body, Query
from starlette import status
from typing import Annotated

from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_QuestionBank
from Backend.Model.response_model import Res_QuestionBank
from Backend.Business.BO_question_bank import BO_question_bank
from Backend.Business.BO_authenticate import get_current_user
from Backend.Router.question_router import question_router

question_bank_router = APIRouter(prefix='/question_bank', tags=['question_bank'])
question_bank_router.include_router(question_router)


# INSERT
@question_bank_router.post('/', status_code=status.HTTP_200_OK)
async def insert_question_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                               data: Annotated[Req_QuestionBank, Body()],
                               question_bank_service: Annotated[BO_question_bank, Depends()]) -> str:
    try:
        return question_bank_service.insert_question_bank(teacher_id=teacher.id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# SELECT
@question_bank_router.get('/', status_code=status.HTTP_200_OK)
async def get_question_banks_by_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                                           collection_id: Annotated[str, Query(min_length=8, max_length=8)],
                                           question_bank_service: Annotated[BO_question_bank, Depends()]):
    try:
        return [Res_QuestionBank.from_DB_model(question_bank) for question_bank in
                question_bank_service.get_question_banks_by_collection(teacher_id=teacher.id,
                                                                       collection_id=collection_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# UPDATE
@question_bank_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_question_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                               data: Annotated[Req_QuestionBank, Body()],
                               question_bank_service: Annotated[BO_question_bank, Depends()]):
    try:
        question_bank_service.update_question_bank(teacher_id=teacher.id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
