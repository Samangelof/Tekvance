# gui/utils/image_loader.py
"""
Высокоуровневые функции для безопасной загрузки изображений с использованием customtkinter.
"""

import customtkinter
from .image_utils import load_image, create_placeholder_image


def safe_load_image(path_light=None, path_dark=None, size=(20, 20)):
    """
    Загрузка пары light/dark изображений с использованием плейсхолдера при ошибке.
    Возвращается customtkinter.CTkImage с заданным размером.

    :param path_light: Путь до light-версии изображения.
    :param path_dark: Путь до dark-версии изображения.
    :param size: Размер изображения (ширина, высота).
    :return: customtkinter.CTkImage объект.
    """
    light_image = load_image(path_light, size) if path_light else create_placeholder_image(size)
    dark_image = load_image(path_dark, size) if path_dark else create_placeholder_image(size)
    
    return customtkinter.CTkImage(light_image=light_image, dark_image=dark_image, size=size)


def safe_load_single_image(path, size=(26, 26)):
    """
    Загрузка одного изображения с использованием плейсхолдера при ошибке.
    Возвращается customtkinter.CTkImage с заданным размером.

    :param path: Путь до изображения.
    :param size: Размер изображения (ширина, высота).
    :return: customtkinter.CTkImage объект.
    """
    image = load_image(path, size)
    return customtkinter.CTkImage(image, size=size)