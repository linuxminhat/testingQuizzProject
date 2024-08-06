from fastapi import APIRouter, HTTPException, Depends, Body, File, UploadFile
from starlette import status
from typing import Annotated
from Backend.Model.DB_model import Student
from Backend.Model.request_model import Req_Student
from Backend.Model.response_model import Res_Student
from Backend.Business.BO_student import BO_student
from Backend.Business.BO_authenticate import get_current_user
from Backend.Router.group_router import student_group_router
from Backend.Router.group_test_router import student_group_test_router

student_router = APIRouter(prefix='/student', tags=['student'])
student_router.include_router(student_group_router)
student_router.include_router(student_group_test_router)


@student_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Student, Body()],
                  student_service: Annotated[BO_student, Depends()]) -> str:
    try:
        return student_service.sign_up(data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.get('/', status_code=status.HTTP_200_OK, response_model_exclude_unset=True)
async def get_student(student: Annotated[Student, Depends(get_current_user)],
                      student_service: Annotated[BO_student, Depends()]):
    try:
        return Res_Student.from_DB_model(student_service.get_student_by_id(student.id))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.patch('/information', status_code=status.HTTP_200_OK)
async def update(student: Annotated[Student, Depends(get_current_user)],
                 data: Annotated[Req_Student, Body()],
                 student_service: Annotated[BO_student, Depends()]):
    try:
        data.id = student.id
        student_service.update_student(data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@student_router.put('/avatar', status_code=status.HTTP_201_CREATED)
async def update_avatar(student: Annotated[Student, Depends(get_current_user)],
                        image: Annotated[UploadFile, File(description="Upload avatar")],
                        student_service: Annotated[BO_student, Depends()]):
    try:
        return await student_service.update_avatar(student_id=student.id, image=image)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
