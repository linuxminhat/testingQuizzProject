from fastapi import APIRouter, HTTPException, Depends, Body, File, UploadFile
from starlette import status
from typing import Annotated

from Backend.Model.DB_model import Teacher
from Backend.Model.request_model import Req_Teacher
from Backend.Model.response_model import Res_Teacher
from Backend.Business.BO_authenticate import get_current_user
from Backend.Business.BO_teacher import BO_teacher
from Backend.Router.collection_router import collection_router
from Backend.Router.group_router import teacher_group_router
from Backend.Router.group_test_router import teacher_group_test_router

teacher_router = APIRouter(prefix='/teacher', tags=['teacher'])
teacher_router.include_router(collection_router)
teacher_router.include_router(teacher_group_router)
teacher_router.include_router(teacher_group_test_router)


@teacher_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Teacher, Body()],
                  teacher_service: Annotated[BO_teacher, Depends()]):
    try:
        return teacher_service.sign_up(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_router.get('/', status_code=status.HTTP_200_OK)
async def get_teacher(teacher: Annotated[Teacher, Depends(get_current_user)],
                      teacher_service: Annotated[BO_teacher, Depends()]):
    try:
        return Res_Teacher.from_DB_model(teacher_service.get_teacher_by_id(teacher.id))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_router.patch('/information', status_code=status.HTTP_200_OK)
async def update(teacher: Annotated[Teacher, Depends(get_current_user)],
                 data: Annotated[Req_Teacher, Body()],
                 teacher_service: Annotated[BO_teacher, Depends()]):
    try:
        data.id = teacher.id
        teacher_service.update_teacher(data=data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@teacher_router.put('/avatar', status_code=status.HTTP_201_CREATED)
async def update_avatar(image: Annotated[UploadFile, File(description="Upload avatar")],
                        teacher: Annotated[Teacher, Depends(get_current_user)],
                        teacher_service: Annotated[BO_teacher, Depends()]):
    try:
        return await teacher_service.update_avatar(teacher_id=teacher.id, image=image)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
