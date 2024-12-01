import customtkinter as ctk
from constants import OBJECT_WIDTH, OBJECT_HEIGHT
from registration import register


def init_log_reg_menu(app):
    main_menu_buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
    main_menu_buttons_frame.pack(pady=110, side="bottom")

    text_button_font = ctk.CTkFont(family="Golos Text Demibold", size=14)

    button_login = ctk.CTkButton(main_menu_buttons_frame,
                                 height=OBJECT_HEIGHT,
                                 width=OBJECT_WIDTH,
                                 text="Войти в систему",
                                 font=text_button_font,
                                 corner_radius=30,
                                 fg_color="#2d82e3",
                                 command=None,
                                 )
    button_login.pack()

    button_register = ctk.CTkButton(main_menu_buttons_frame,
                                    height=OBJECT_HEIGHT,
                                    width=OBJECT_WIDTH,
                                    text="Зарегистрироваться",
                                    font=text_button_font,
                                    corner_radius=30,
                                    fg_color="#2d82e3",
                                    command=lambda: register(main_menu_buttons_frame, app),
                                    )
    button_register.pack(pady=(15, 0))