import peewee
from peewee import PostgresqlDatabase
from datetime import datetime


db = PostgresqlDatabase(
    'orm_py25',
    user='tutan',
    password='1',
    host='localhost',
    port=5432
)
