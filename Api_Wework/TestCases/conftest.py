import time

import pytest
from faker import Faker

import os

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))


@pytest.fixture()
def member_info():
    faker = Faker('zh-CN')
    name = faker.name()
    mobile = faker.phone_number()
    userid = str(time.time()) + 'Jen'
    data = [userid, name, mobile]
    return data

@pytest.fixture()
def get_name():
    tag_name = str(time.time()) + 'Elsa'
    return tag_name

@pytest.fixture()
def depart_name():
    faker = Faker('zh_CN')
    depart_name = faker.job()
    return  depart_name




