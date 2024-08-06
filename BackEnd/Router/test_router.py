from fastapi import APIRouter, HTTPException, Depends, Body, Query
from typing import Annotated
from starlette import status

from Backend.Business.BO_test import BO_test
from Backend.Model.DB_model import Teacher
from Backend.Business.BO_authenticate import get_current_user
from Backend.Model.request_model import Req_Test
from Backend.Model.response_model import Res_Test
from Backend.Router.annotate import QUERY_LEN_8

test_router = APIRouter(prefix='/test', tags=['test'])

TEST_SERVICE = Annotated[BO_test, Depends()]

# SELECT
@test_router.get('/', status_code=status.HTTP_200_OK)
async def get_tests(teacher: Annotated[Teacher, Depends(get_current_user)],
                    collection_id: QUERY_LEN_8,
                    test_service: TEST_SERVICE):
    try:
        return [Res_Test.from_DB_model(test) for test in test_service.get_test_by_collection(collection_id, teacher.id)]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# INSERT
@test_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                      data: Annotated[Req_Test, Body()],
                      test_service: TEST_SERVICE) -> str:
    try:
        return test_service.insert_test(teacher.id, data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# UPDATE
@test_router.put('/', status_code=status.HTTP_200_OK)
async def update_test(teacher: Annotated[Teacher, Depends(get_current_user)],
                      test: Annotated[Req_Test, Body()],
                      test_service: TEST_SERVICE,
                      test_id: QUERY_LEN_8):
    try:
        test.id = test_id
        test_service.update_test(teacher.id, test)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))