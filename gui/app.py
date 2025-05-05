import os
from gui.config import load_app_config
import customtkinter as ctk
from gui.core.app_controller import AppController
from gui.core.status_manager import StatusManager
from gui.utils.logger import setup_logging 
from gui.layout.layout_loader import load_layout

logger = setup_logging()


class TekVanceApp(ctk.CTk):
    """
    Основной класс приложения Tekvance.
    Инициализирует окно приложения и координирует работу основных компонентов.
    """
    def __init__(self, config=None):
        super().__init__()
        config = config or load_app_config()
        self.logger = setup_logging()
        
        self.title("Tekvance")
        self.geometry("700x450")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        # ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_default_color_theme(config['color_theme'])



        self.status_manager = StatusManager(self)
        self.app_controller = AppController(self)

        
    def destroy(self):
        """Переопределение метода destroy для корректного завершения работы"""
        self.status_manager.cleanup()
        super().destroy()