import sqlite3
from time import time

from constants import SQLITE_DB


def connect():
    return sqlite3.connect(SQLITE_DB)


def table_exists(table_name):
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("select * from sqlite_master where name = '{}' and type = 'table'".format(table_name))
        return bool(list(cur))


def create_table(table_name):
    with connect() as conn:
        conn.execute("create table temperature (timestamp integer primary key, value real)".format(table_name))


def insert_record(table_name, value: [int, float]):
    if not table_exists(table_name):
        create_table(table_name)
    with connect() as conn:
        current_time = int(time())
        conn.execute("insert into {} values ({}, {})".format(table_name, current_time, value))
