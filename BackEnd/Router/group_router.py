import os

from fastapi import APIRouter, HTTPException, Depends, Body, Query
from starlette import status
from typing import Annotated

from Backend.Business import STATIC_PATH
from Backend.Model.request_model import Req_Group, Req_GroupStudent
from Backend.Model.response_model import Res_Group, Res_Student
from Backend.Model.DB_model import Teacher, Student
from Backend.Business.BO_group import BO_group
from Backend.Business.BO_group_student import BO_group_student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Router.annotate import QUERY_LEN_8, BODY_LEN_8

student_group_router = APIRouter(prefix='/group', tags=['group'])
teacher_group_router = APIRouter(prefix='/group', tags=['group'])


### TEACHER ###
# INSERT GROUP
@teacher_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                       data: Annotated[Req_Group, Body()],
                       group_service: Annotated[BO_group, Depends()]) -> str:
    try:
        data.teacher_id = teacher.id
        return group_service.insert_group(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET GROUPS BY VISIBILITY
@teacher_group_router.get('/', status_code=status.HTTP_200_OK)
async def get_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                    group_service: Annotated[BO_group, Depends()],
                    is_show: Annotated[bool, Query()] = True):
    try:
        return [Res_Group.from_DB_model(group) for group in group_service.get_groups_by_teacher(teacher.id, is_show)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_group_router.get('/static_images', status_code=status.HTTP_200_OK)
async def get_static_images():
    return [os.path.join('Group', 'Images', name) for name in os.listdir(os.path.join(STATIC_PATH, 'Group', 'Images'))]


# UPDATE GROUP
@teacher_group_router.patch('/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                       data: Annotated[Req_Group, Body()],
                       group_service: Annotated[BO_group, Depends()]):
    try:
        data.teacher_id = teacher.id
        group_service.update_group(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# INSERT list[STUDENT] TO GROUP
@teacher_group_router.post('/student', status_code=status.HTTP_201_CREATED)
async def insert_students(teacher: Annotated[Teacher, Depends(get_current_user)],
                          data: Annotated[Req_GroupStudent.Req_InsertedInformation, Body()],
                          group_id: QUERY_LEN_8,
                          group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.insert_students(teacher_id=teacher.id, group_id=group_id, data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET STUDENTS IN GROUP
@teacher_group_router.get('/student', status_code=status.HTTP_200_OK)
async def get_students_in_group(teacher: Annotated[Teacher, Depends(get_current_user)],
                                group_student_service: Annotated[BO_group_student, Depends()],
                                group_id: QUERY_LEN_8,
                                is_join: Annotated[bool, Query()] = True):
    try:
        return [Res_Student.from_DB_model(student) for student in
                group_student_service.get_students_by_group(teacher_id=teacher.id, group_id=group_id, is_join=is_join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE STUDENTS IN GROUP
@teacher_group_router.delete('/student', status_code=status.HTTP_204_NO_CONTENT)
async def delete_students(teacher: Annotated[Teacher, Depends(get_current_user)],
                          group_id: QUERY_LEN_8,
                          list_id: Annotated[list[BODY_LEN_8], Body()],
                          group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.delete_students(teacher_id=teacher.id, group_id=group_id, list_id=list_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


### STUDENT ###
@student_group_router.get('/', status_code=status.HTTP_200_OK)
async def get_groups(student: Annotated[Student, Depends(get_current_user)],
                     group_student_service: Annotated[BO_group_student, Depends()],
                     join: Annotated[bool, Query()] = True):
    try:
        return [Res_Group.from_DB_model(group) for group in
                group_student_service.get_groups_by_student(student_id=student.id, is_join=join)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.get('/students', status_code=status.HTTP_200_OK)
async def get_other_students_in_group(student: Annotated[Student, Depends(get_current_user)],
                                      group_id: QUERY_LEN_8,
                                      group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        return [Res_Student.from_DB_model(student) for student in group_student_service.get_other_students_by_group(student.id, group_id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.post('/', status_code=status.HTTP_201_CREATED)
async def request_join_group(student: Annotated[Student, Depends(get_current_user)],
                             group_id: QUERY_LEN_8,
                             group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.request_join(group_id=group_id, student_id=student.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_student_group(student: Annotated[Student, Depends(get_current_user)],
                               data: Annotated[Req_GroupStudent, Body()],
                               group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        data.student_id = student.id
        group_student_service.update_student_group(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_group_router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def leave_group(student: Annotated[Student, Depends(get_current_user)],
                      group_id: QUERY_LEN_8,
                      group_student_service: Annotated[BO_group_student, Depends()]):
    try:
        group_student_service.leave_group(student.id, group_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
