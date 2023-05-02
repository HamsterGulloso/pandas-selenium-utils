from pandas import DataFrame
from typing import Literal
from sqlalchemy import Engine

def engine(
        user: str,
        host: str,
        database: str,
        password:str = None
    ) -> Engine:
    ...

def insert(
    dataframe: DataFrame,
    user: str,
    host: str,
    database: str,
    table: str,
    password: str = None,
    behavior: Literal["append", "replace", "fail"] = "fail"
) -> None:
    ...

def read(
    user: str,
    host: str,
    database: str,
    table: str,
    password: str = None
) -> DataFrame:
    ...

def update(
    dataframe: DataFrame,
    user: str,
    host: str,
    database: str,
    table: str,
    update_on: list[str],
    password: str = None
) -> None:
    ...