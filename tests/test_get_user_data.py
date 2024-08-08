import requests, allure
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"

@allure.title('проверяем получение списка пользователей')
def test_list_users():
    with allure.step("делаем запрос по адресу"):
        response = requests.get(BASE_URL + LIST_USERS)
    #print(response.json())
    with allure.step("hkhh"):
        assert response.status_code == 200

    data = response.json()['data']
    for i in data:
        with allure.step("check item list"):
            validate(i, USER_DATA_SCHEME)
            with allure.step("check end email adress"):
                assert i['email'].endswith('.org')