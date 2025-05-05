from gui.frames.home import HomeFrame
from gui.frames.frame2 import Frame2
from gui.frames.frame3 import Frame3
from gui.navigation import NavigationPanel
from gui.utils.button_factory import ButtonFactory

import customtkinter as ctk

class AppController:
    """
    Контроллер приложения, отвечает за управление фреймами и навигацией.
    Обеспечивает переключение между различными экранами приложения.
    """
    def __init__(self, master):
        self.master = master

        self.frames = {
            "home": HomeFrame(master),
            "frame_2": Frame2(master),
            "frame_3": Frame3(master)
        }
        
        for frame in self.frames.values():
            frame.grid(row=0, column=1, sticky="nsew")
            frame.grid_remove()
        
        button_factory = ButtonFactory()
        self.navigation = NavigationPanel(master, self.select_frame_by_name, button_factory)
        self.navigation.grid(row=0, column=0, sticky="nsew")
        
        #* Отображение начального фрейма
        self.select_frame_by_name("home")
    
    def select_frame_by_name(self, name):
        """
        Переключает активный фрейм.
        
        :param name: Идентификатор фрейма для отображения
        """
        for key, frame in self.frames.items():
            if key == name:
                frame.grid()
            else:
                frame.grid_remove()
        self.navigation.update_selection(name)