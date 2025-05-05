import customtkinter
import os
from gui.utils.image_loader import safe_load_single_image, safe_load_image
from gui.utils.button_factory import ButtonFactory
from gui.utils.button_config import NAV_BUTTONS


class NavigationPanel(customtkinter.CTkFrame):
    def __init__(self, master, select_callback, button_factory: ButtonFactory):
        super().__init__(master, corner_radius=0)
        self.select_callback = select_callback
        self.button_factory = button_factory
        
        image_path = os.path.join(os.path.dirname(__file__), "images")

        self.grid_rowconfigure(4, weight=1)

        self.logo_image = safe_load_single_image(os.path.join(image_path, "CustomTkinter_logo_single.png"), size=(26, 26))

        customtkinter.CTkLabel(self, text="  Tekvance", image=self.logo_image,
                               compound="left", font=customtkinter.CTkFont(size=15, weight="bold")).grid(row=0, column=0, padx=20, pady=20)

        self.buttons = {}

        for i, (key, cfg) in enumerate(NAV_BUTTONS.items(), start=1):
            print(cfg)
            icon = safe_load_image(
                # Словил микроинсульт на этом 
                path_light=os.path.join(image_path, cfg["icon_dark"]), # темная иконка для light_theme
                path_dark=os.path.join(image_path, cfg["icon_light"]), # белая иконка для dark_theme
                size=(20, 20)
            )

            btn = self.button_factory.create_button(
                self, icon, cfg["text"], key, self.select_callback
            )
            btn.configure(
                corner_radius=0, height=40, border_spacing=10,
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30")
            )
            btn.grid(row=i, column=0, sticky="ew")

            self.buttons[key] = btn
            print(f"Creating button for {key} with icon light: {cfg['icon_light']} and icon dark: {cfg['icon_dark']}")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                                command=customtkinter.set_appearance_mode)
        self.appearance_mode_menu.grid(row=i+1, column=0, padx=20, pady=20, sticky="s")
        print(f"Current theme: {customtkinter.get_appearance_mode()}")

    def update_selection(self, active_key):
        for key, btn in self.buttons.items():
            btn.configure(fg_color=("gray75", "gray25") if key == active_key else "transparent")
