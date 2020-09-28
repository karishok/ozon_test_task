import allure
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post(response, key, key_value):
    _response_general_check(response)
    print(key, key_value)
    if isinstance(response.json(), list):
        res = response.json()[0][key]
    else:
        res = response.json()[key]
    assert_that(res, equal_to(key_value), "Wrong post return from server")


@allure.step
def check_status_code(response):
    _response_general_check(response)


@allure.step
def check_add_post(payload, response):
    _response_general_check(response, expected_code=codes.created)
    assert_that(response.json(), payload, "Wrong response from server")
