from sqlalchemy import create_engine, URL
from pandas import read_sql_table


def engine(user, host, database, password = None):
    try:
        return create_engine(URL.create(
            "mysql",
            user,
            password,
            host,
            database=database
        ))
    except ModuleNotFoundError:
        pass
    
    try:
        return create_engine(URL.create(
            "mysql+mysqldb",
            user,
            password,
            host,
            database=database
        ))
    except ModuleNotFoundError:
        pass

    try:
        return create_engine(URL.create(
            "mysql+pymysql",
            user,
            password,
            host,
            database=database
        ))
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Install: pymysql, MySQL-python or mysqlclient")


def insert(dataframe, user, host, database, table, password = None, behavior = "fail"):
    if behavior.lower() not in ("replace", "append", "fail"):
        raise ValueError("Behavior is improper:\nValid: [replace | append | fail]")
    
    ng = engine(user, host, database, password)

    with ng.connect() as con:
        dataframe.to_sql(table, con=con, if_exists=behavior, index=False)
        con.commit()

def update(dataframe, user, host, database, table, update_on = None, password = None):
    if type(update_on) != list:
        raise ValueError("Update_on must me set as a list with column names")
    for c in update_on:
        if c not in dataframe.columns:
            raise ValueError(f"{c} not in dataframe columns")
    ng = engine(user, host, database, password)
    with ng.connect() as con:
        for line in dataframe.iterrows():
            sets = ", ".join([f"{cols} = '{value}'" for cols, value in line[1].items() if cols not in update_on])
            where = " and ".join([f"{cols} = '{value}'" for cols, value in line[1].items() if cols in update_on])
            con.exec_driver_sql(f"update {table} set {sets} where {where}")
            con.commit()

def read(user, host, database, table, password = None):
    ng = engine(user, host, database, password)
    with ng.connect() as con:
        return read_sql_table(
            table,
            con
        )