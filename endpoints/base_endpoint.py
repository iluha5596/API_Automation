import allure


class Endpoint:
    response = None
    response_json = None

    def check_response_is_200(self):
        with allure.step('Проверка, что код ответа == 200'):
            assert self.response.status_code == 200
