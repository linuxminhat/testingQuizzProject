from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated
from starlette import status

from Backend.Business.BO_group_test import BO_group_test
from Backend.Business.BO_student_test import BO_student_test
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_GroupTest
from Backend.Model.response_model import Res_GroupTest, Res_StudentTest
from Backend.Router.annotate import QUERY_LEN_8

teacher_group_test_router = APIRouter(prefix='/grouptest', tags=['grouptest'])
student_group_test_router = APIRouter(prefix='/grouptest', tags=['grouptest'])


### TEACHER ###
# INSERT
@teacher_group_test_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_GroupTest, Body()],
                            group_test_service: Annotated[BO_group_test, Depends()]):
    try:
        return group_test_service.insert_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# SELECT
@teacher_group_test_router.get('/', status_code=status.HTTP_200_OK)
@student_group_test_router.get('/', status_code=status.HTTP_200_OK)
async def get_group_test(_: Annotated[Teacher | Student, Depends(get_current_user)],
                         group_test_service: Annotated[BO_group_test, Depends()],
                         group_id: Annotated[str, Query(min_length=8, max_length=8)]):
    try:
        return [Res_GroupTest.from_DB_model(group_test) for group_test in
                group_test_service.get_group_test_in_group(group_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_test_router.get('/student_test', status_code=status.HTTP_200_OK)
async def get_studentworks(teacher: Annotated[Teacher, Depends(get_current_user)],
                           group_test_service: Annotated[BO_group_test, Depends()],
                           group_test_id: QUERY_LEN_8):
    try:
        # if student_id is not None:
        #     return Res_StudentTest.from_DB_model(group_test_service.get_studentwork(group_test_id, student_id))

        return [Res_StudentTest.from_DB_model(student_test) for student_test in
                group_test_service.get_student_tests(group_test_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @teacher_group_test_router.get('/studentpoint', status_code=status.HTTP_200_OK)
# async def get_studentpoint(teacher: Annotated[Teacher, Depends(get_current_user)],
#                            group_test_service: Annotated[BO_group_test, Depends()],
#                            group_test_id: Annotated[str, Query(min_length=8, max_length=8)]):
#     try:
#         return [Res_StudentScore(student_id=sp[0].id, name=sp[0].name, avatar_path=sp[0].avatar_path, point=sp[1]) for
#                 sp in
#                 group_test_service.get_students_scores(group_test_id)]
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# UPDATE
@teacher_group_test_router.put('/', status_code=status.HTTP_200_OK)
async def update_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_service: Annotated[BO_group_test, Depends()],
                            data: Annotated[Req_GroupTest, Body()]):
    try:
        group_test_service.update_group_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE
@teacher_group_test_router.delete('/teacher', status_code=status.HTTP_200_OK)
async def delete_group_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                            group_test_id: Annotated[str, Query(min_length=8, max_length=8)],
                            group_test_service: Annotated[BO_group_test, Depends()]):
    try:
        group_test_service.delete_group_test(teacher.id, group_test_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


### STUDENT ###
@teacher_group_test_router.get('/calendar', status_code=status.HTTP_200_OK)
@student_group_test_router.get('/calendar', status_code=status.HTTP_200_OK)
async def get_group_test_in_time(user: Annotated[Student | Teacher, Depends(get_current_user)],
                                 group_test_service: Annotated[BO_group_test, Depends()],
                                 start: Annotated[datetime, Query()],
                                 end: Annotated[datetime, Query()]):
    try:
        return [Res_GroupTest.from_DB_model(group_test) for group_test in
                group_test_service.get_group_test_calendar('teacher' if isinstance(user, Teacher) else 'student', user.id, start, end)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @student_group_test_router.get('/studentwork/', status_code=status.HTTP_200_OK)
# async def get_student_test(student: Annotated[Student, Depends(get_current_user)],
#                            group_test_service: Annotated[BO_student_test, Depends()],
#                            group_test_id: QUERY_LEN_8):
#     try:
#         return Res_StudentTest.from_DB_model(group_test_service.get_student_test_by_group_test_id(student.id, group_test_id))
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# @student_group_test_router.post('/studentwork/submit', status_code=status.HTTP_200_OK)
# async def update_student_work(student: Annotated[Student, Depends(get_current_user)],
#                               data: Annotated[Req_StudentWork, Body()],
#                               group_test_service: Annotated[BO_student_test, Depends()]) -> float:
#     try:
#         return group_test_service.submit(student.id, data)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_test_router.get('/history', status_code=status.HTTP_200_OK)
async def get_history(student: Annotated[Student, Depends(get_current_user)],
                      group_test_service: Annotated[BO_student_test, Depends()],
                      group_id: QUERY_LEN_8):
    try:
        return [Res_StudentTest.from_DB_model(student_test) for student_test in
                group_test_service.get_history(student.id, group_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
