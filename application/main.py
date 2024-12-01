import customtkinter as ctk
from PIL import Image
from log_reg_menu import init_log_reg_menu


app = ctk.CTk()
ctk.set_appearance_mode("light")
app.title("Моя Библиотека")
app.geometry("640x480")
app.resizable(width=False, height=False)
app.iconbitmap("../images./logo.ico")
image = Image.open("../images/background.jpeg")
background_image = ctk.CTkImage(image, size=(640, 480))
background_image_label = ctk.CTkLabel(app, text="", image=background_image)
background_image_label.place(x=0, y=0)

init_log_reg_menu(app)

if __name__ == "__main__":
    app.mainloop()