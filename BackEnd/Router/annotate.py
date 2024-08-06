from typing import Annotated

from fastapi import Query, Body

QUERY_LEN_8 = Annotated[str, Query(min_length=8, max_length=8)]
QUERY_LEN_10 = Annotated[str, Query(min_length=10, max_length=10)]
BODY_LEN_8 = Annotated[str, Body(min_length=8, max_length=8)]