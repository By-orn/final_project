import configuration
import requests
import requests_data


# Функция, которая отправляет POST запрос для создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=requests_data.headers)


# Функция, которая отправляет GET запрос на получение заказа по его трек номеру
def get_order(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + order_track,
                        headers=requests_data.headers)
