import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


def _get(path: str):
    return r.get(url=JSONPLACEHOLDER_HOST + path)


def _post(payload, headers, path):
    return r.post(url=JSONPLACEHOLDER_HOST + path, headers=headers, data=payload)


class Client:
    @allure.step
    def get_all_posts(self):
        return _get(path=f'/posts')

    @allure.step
    def get_posts_by_id(self, post_id: int):
        return _get(path=f'/posts/{post_id}')

    @allure.step
    def post_new_posts(self, payload):
        headers = {}
        path = "/posts"
        return _post(payload, headers, path)

    @allure.step
    def get_posts_by_user_id(self, user_id: int):
        return _get(path=f'/posts?userId={user_id}')

    @allure.step
    def get_only_completed_todos(self, is_completed: str):
        return _get(path=f'/todos?completed={is_completed}')
