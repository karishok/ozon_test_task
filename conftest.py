import pytest
from random import choice, randint
from string import printable


@pytest.fixture(scope="function")
def generate_post():
    return {
        "id": randint(100, 140),
        "userId": randint(1, 11),
        "title": ''.join(choice(printable) for i in range(randint(5, 30))),
        "body": ''.join(choice(printable) for i in range(randint(20, 50)))
    }
