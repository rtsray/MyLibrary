import customtkinter as ctk
import re

import psycopg2
from config import host, user, password, db_name, port

from constants import OBJECT_WIDTH, OBJECT_HEIGHT, PV_ERROR_LEN, LV_ERROR_LEN, LV_ERROR_SYMB


def register(main_menu_buttons_frame, app):
    main_menu_buttons_frame.destroy()

    register_menu_buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
    register_menu_buttons_frame.pack(pady=(0, 50), side="bottom")

    entry_login = ctk.CTkEntry(register_menu_buttons_frame,
                                      fg_color="transparent",
                                      corner_radius=30,
                                      height=OBJECT_HEIGHT,
                                      width=OBJECT_WIDTH,
                                      placeholder_text="Введите логин",
                                      )
    entry_login.pack()

    entry_password = ctk.CTkEntry(register_menu_buttons_frame,
                                      fg_color="transparent",
                                      corner_radius=30,
                                      height=OBJECT_HEIGHT,
                                      width=OBJECT_WIDTH,
                                      placeholder_text="Введите пароль",
                                      show="*",
                                      )
    entry_password.pack(pady=(15, 0))


    error_font = ctk.CTkFont(family="Golos Text", size=14)

    error_label = ctk.CTkLabel(register_menu_buttons_frame,
                               text="",
                               text_color="#cc4545",
                               font=error_font
                               )
    error_label.pack(pady=(15, 0))


    def pv_error():
        error_label.configure(text=PV_ERROR_LEN)


    def lv_error(user_login):
        if len(user_login) < 4:
            error_label.configure(text=LV_ERROR_LEN)
        else:
            error_label.configure(text=LV_ERROR_SYMB)


    def password_validate(user_password):
        if len(user_password) > 6:
            return True
        else:
            pv_error()
            return False


    def login_validate(user_login):
        pattern = r'[^a-zA-Z0-9]'
        if not bool(re.search(pattern, user_login)) and len(user_login) > 3:
            return True
        else:
            lv_error(user_login)
            return False


    def send_data():
        user_password = str(entry_password.get())
        user_login = str(entry_login.get())

        error_label.configure(text="")

        if password_validate(user_password) and login_validate(user_login):
            try:
                connection = psycopg2.connect(
                    password=password,
                    host=host,
                    port=port,
                    user=user,
                    database=db_name,
                )

                with connection.cursor() as cursor:
                    cursor.execute('INSERT INTO "Users" (login, password) VALUES (%s, %s);', (user_login, user_password))
                    connection.commit()
                    print("[INFO] An account has been successfully created.")

            except Exception as ex:
                print("[INFO] Something went wrong with Postgres: ", ex)

            finally:
                if connection:
                    connection.close()
                    print("[INFO] Postgres closed.")


    button_send_data_font = ctk.CTkFont(family="Golos Text Demibold", size=14)

    button_send_data = ctk.CTkButton(register_menu_buttons_frame,
                                     height=OBJECT_HEIGHT,
                                     width=OBJECT_WIDTH - 50,
                                     text="Продолжить",
                                     corner_radius=30,
                                     font=button_send_data_font,
                                     command=send_data,
                                     )
    button_send_data.pack(pady=(15, 0))
