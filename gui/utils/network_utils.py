# gui/utils/networks_utils.py
"""
Низкоуровневые утилиты для проверки интернет-соединения.

Содержит функции для теста доступности внешних ресурсов через TCP и HTTP.
"""

import socket
import requests


def check_internet_ping(host="8.8.8.8", port=53, timeout=3):
    """
    Проверяет наличие подключения к интернету.

    Попытка установить TCP-соединение с указанным хостом и портом.
    По умолчанию пингуется DNS-сервер Google (8.8.8.8:53).

    Параметры:
        host (str): Хост для подключения. По умолчанию "8.8.8.8".
        port (int): Порт для подключения. По умолчанию 53 (DNS).
        timeout (int | float): Таймаут в секундах для попытки подключения.

    Возвращает:
        bool: True если соединение успешно, False если нет.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


def check_internet_http(url="http://clients3.google.com/generate_204", timeout=5):
    """
    Проверяет наличие интернет-соединения через HTTP-запрос.

    По умолчанию обращается к Google URL, который возвращает пустой ответ с кодом 204.

    Аргументы:
        url (str): URL для проверки. По умолчанию Google (204 No Content).
        timeout (float): Таймаут запроса в секундах. По умолчанию 5.

    Возвращает:
        bool: True — если ответ получен, False — если нет.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 204
    except requests.RequestException:
        return False