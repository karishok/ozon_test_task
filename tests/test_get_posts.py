import allure
from framework.check import check_add_post, check_get_all_posts_response, check_status_code, check_get_post
from framework.jsonplaceholder_client import Client
from framework.helper import get_random_post
import pytest


@allure.suite('GET')
class TestGetPosts:

    # позитивный тест на получение всех постов
    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check_get_all_posts_response(response)

    # позитивный тест на получение конкретного поста (GET)
    # генерация данных в helper
    @allure.title('Positive. Get post by id')
    def test_positive_get_post_by_id(self):
        post_id = get_random_post()
        response = Client().get_posts_by_id(post_id)
        check_get_post(response, "id", post_id)

    # негативный тест на получение конкретного поста (GET)
    @allure.title('Negative. Get post by id')
    @pytest.mark.xfail
    def test_negative_get_post_by_id(self):
        post_id = 120
        response = Client().get_posts_by_id(post_id)
        check_status_code(response)

    # тест с параметризацей
    # позитивный и негативный тест на получение поста по user_id (GET)
    @allure.title('Positive and negative. Get post by user_id')
    @pytest.mark.parametrize('user_id', [2,
                                         7,
                                         9,
                                         pytest.param(11, marks=pytest.mark.xfail)])
    def test_get_post_by_user_id(self, user_id):
        response = Client().get_posts_by_user_id(user_id)
        check_get_post(response, "userId", user_id)

    #  свой тест на получение завершенных todos
    @allure.title('Positive. Get completed todos')
    def test_get_only_completed_todos(self):
        is_completed = "true"
        response = Client().get_only_completed_todos(is_completed)
        check_status_code(response)


@allure.suite('POST')
class TestSendPosts:
    # фикстура для генерации поста
    # позитивный тест на добавление нового поста (POST)
    @allure.title('Positive. Add new post')
    def test_positive_add_post(self, generate_post):
        payload = generate_post
        print(payload)
        response = Client().post_new_posts(payload)
        check_add_post(payload, response)
