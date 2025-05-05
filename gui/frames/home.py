import os
import customtkinter
from gui.utils.image_loader import safe_load_single_image


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
    
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
        
        large_image = safe_load_single_image(os.path.join(image_path, "large_test_image.png"), size=(500, 150))
        icon_image = safe_load_single_image(os.path.join(image_path, "image_icon_light.png"), size=(20, 20))

        customtkinter.CTkLabel(self, text="", image=large_image).grid(row=0, column=0, padx=20, pady=10)
        
        for i in range(4):
            customtkinter.CTkButton(self, text=f"Button {i+1}", image=icon_image).grid(row=i+1, column=0, padx=20, pady=10)
