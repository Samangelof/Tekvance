import customtkinter


class Frame2(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        customtkinter.CTkLabel(self, text="Frame 2").pack(pady=20)
