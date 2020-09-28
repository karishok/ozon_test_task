import pytest
from random import randint, sample
from string import printable


@pytest.fixture(scope="function")
def generate_post():
    return {
        "id": randint(100, 140),
        "userId": randint(1, 11),
        "title": ''.join(sample(printable, randint(5, 30))),
        "body": ''.join(sample(printable, randint(20, 50)))
    }
