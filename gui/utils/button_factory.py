import customtkinter


class ButtonFactory:
    def __init__(self, default_style=None):
        """
        Инициализация фабрики кнопок с дефолтным стилем.
        
        :param default_style: Дефолтный стиль кнопки. Если не передан, используется набор параметров по умолчанию.
        """
        self.default_style = default_style or {
            "corner_radius": 0,
            "height": 40,
            "border_spacing": 10,
            "fg_color": "transparent",
            "text_color": ("gray10", "gray90"),
            "hover_color": ("gray70", "gray30")
        }

    def create_button(self, master, image, text, key, select_callback, **custom_style):
        """
        Создание кнопки с использованием дефолтного стиля и кастомных изменений.
        
        :param master: Родительский виджет, в котором будет размещена кнопка.
        :param image: Изображение для кнопки.
        :param text: Текст на кнопке.
        :param key: Уникальный ключ для кнопки, передаваемый в коллбек.
        :param select_callback: Функция-обработчик, вызываемая при нажатии на кнопку.
        :param custom_style: Кастомные стили для кнопки. Все переданные параметры будут переопределять дефолтные.
        :return: Объект customtkinter.CTkButton.
        """
        button_style = {**self.default_style, **custom_style}

        return customtkinter.CTkButton(
            master=master,
            text=text,
            image=image,
            anchor="w",
            command=lambda: select_callback(key),
            **button_style
        )