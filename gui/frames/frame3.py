import customtkinter


class Frame3(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        customtkinter.CTkLabel(self, text="Frame 3").pack(pady=20)
