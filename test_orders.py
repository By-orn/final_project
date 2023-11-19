# Никита Кузнецов, 10 Земля — Финальный проект. Инженер по тестированию плюс
import api_requests
import requests_data


# Функция, которая создает заказ и сохраняет его трек номер в переменную order_track
def create_order():
    order_body = requests_data.order_body.copy()
    created_order = api_requests.post_new_order(order_body)

    assert created_order.status_code == 201

    order_track = created_order.json()["track"]

    return order_track


# Тест, в рамках которого проверяется получение информации о заказе по его трек номеру
def test_get_order_by_track_number():
    order_track = create_order()
    track_number = "?t=" + str(order_track)

    order_info = api_requests.get_order(track_number)

    assert order_info.status_code == 200
