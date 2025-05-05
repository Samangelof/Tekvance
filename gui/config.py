import os


def load_app_config():
    """
    Загружает конфигурацию для приложения TekVance из переменных окружения.
    Возвращает словарь с настройками.
    """
    return {
        'appearance_mode': os.environ.get('APPEARANCE_MODE', 'System'),
        'color_theme': os.environ.get('COLOR_THEME', 'gui/layout/themes/tekvance_theme.json'),
    }
