# gui/utils/image_utils.py
"""
Низкоуровневые утилиты для работы с изображениями через PIL.
"""

import os
from PIL import Image, ImageDraw


def load_image(path: str, size: tuple = None) -> Image.Image:
    """
    Загрузка изображения по указанному пути с опциональным изменением размера.
    При ошибке загрузки — использование плейсхолдера.

    :param path: Путь до изображения.
    :param size: Размер для ресайза (ширина, высота). Если None — оригинальный размер.
    :return: PIL.Image объект.
    """
    
    try:
        image = Image.open(path)
    except (FileNotFoundError, OSError):
        image = create_placeholder_image(size)
    return image.resize(size) if size else image


def create_placeholder_image(size=(100, 100)) -> Image.Image:
    """
    Генерация плейсхолдер-изображения заданного размера с текстом 'Not found'.

    :param size: Размер изображения (ширина, высота).
    :return: PIL.Image объект.
    """
    width, height = size
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)
    draw.text((width // 4, height // 4), "Not found", fill="black")
    return image
