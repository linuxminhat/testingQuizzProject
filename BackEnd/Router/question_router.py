from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body, Query, UploadFile, File
from starlette import status
from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_Question
from Backend.Model.response_model import Res_Question, Res_NumberOfQuestion
from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_question import BO_question
from Backend.Router.annotate import QUERY_LEN_8, QUERY_LEN_10

question_router = APIRouter(prefix='/question', tags=['question'])

QUESTION_SERVICE = Annotated[BO_question, Depends()]

# INSERT
# update: 2024-05-18: change the Req_Question format
@question_router.post('/', status_code=status.HTTP_200_OK)
async def insert_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: Annotated[str, Query(min_length=8, max_length=8)],
                           data: Annotated[list[Req_Question], Body()],
                           question_service: QUESTION_SERVICE):
    try:
        return question_service.insert_questions(teacher_id=teacher.id, question_bank_id=question_bank_id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.post('/attachment', status_code=status.HTTP_200_OK)
async def insert_attachment(teacher: Annotated[Teacher, Depends(get_current_user)],
                            question_id: QUERY_LEN_10,
                            attachment: Annotated[list[UploadFile], File()],
                            question_service: QUESTION_SERVICE):
    try:
        return await question_service.insert_attachment(teacher_id=teacher.id, question_id=question_id,
                                                        attachment=attachment)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@question_router.get('/', status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_questions_in_bank(teacher: Annotated[Teacher, Depends(get_current_user)],
                                question_bank_id: QUERY_LEN_8,
                                question_service: QUESTION_SERVICE,
                                offset: int = Query(default=1, ge=1),
                                length: int = Query(default=50, ge=1, le=100)):
    try:
        return [Res_Question.from_DB_model(question) for question in
                question_service.get_questions_in_bank(teacher_id=teacher.id, question_bank_id=question_bank_id,
                                                       offset=offset, length=length)]

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.get('/summary', status_code=status.HTTP_200_OK)
async def question_summary(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: QUERY_LEN_8,
                           question_service: QUESTION_SERVICE):
    try:
        return [Res_NumberOfQuestion.from_DB_model(noq) for noq in question_service.summary(teacher_id=teacher.id, question_bank_id=question_bank_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
@question_router.put('/', status_code=status.HTTP_200_OK)
async def update_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: QUERY_LEN_8,
                           data: Annotated[list[Req_Question], Body()],
                           question_service: QUESTION_SERVICE) -> None:
    try:
        question_service.update_questions(teacher_id=teacher.id, question_bank_id=question_bank_id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE
@question_router.delete('/', status_code=status.HTTP_200_OK)
async def delete_questions(teacher: Annotated[Teacher, Depends(get_current_user)],
                           question_bank_id: QUERY_LEN_8,
                           list_id: Annotated[list[str], Body()],
                           question_service: QUESTION_SERVICE) -> None:
    try:
        question_service.delete_questions(teacher_id=teacher.id, question_bank_id=question_bank_id, question_ids=list_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@question_router.delete('/attachment', status_code=status.HTTP_200_OK)
async def delete_attachment(teacher: Annotated[Teacher, Depends(get_current_user)],
                            attachment_path: Annotated[str, Body()],
                            question_service: QUESTION_SERVICE) -> None:
    try:
        question_service.delete_attachment(teacher_id=teacher.id, attachment_path=attachment_path)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
