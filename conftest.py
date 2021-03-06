import os

import pytest

from src.api.db.connection import db
from src.api.db.classinfo import ClassInfo
from src.api.db.courses import Courses
from src.api.db.admin import Admin

TEST_CSV = os.environ.get('TEST_CSV', None)

@pytest.fixture(scope="session")
def db_conn():
    return db

@pytest.fixture(scope="session")
def class_info(db_conn):
    return ClassInfo(db_conn)

@pytest.fixture(scope="session")
def admin_settings(db_conn):
    return Admin(db_conn)

if TEST_CSV is not None:
    with open(TEST_CSV) as csvfile:
        Courses(db).populate_from_csv(csvfile)
