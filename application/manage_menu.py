import customtkinter as ctk

from constants import OBJECT_MM_HEIGHT, OBJECT_MM_WIDTH
from libs_frame import check_libs


manage_menu = ctk.CTk()
ctk.set_appearance_mode("light")
manage_menu.title("Моя Библиотека")
manage_menu.geometry("640x480")
manage_menu.resizable(width=False, height=False)
manage_menu.iconbitmap("../images./logo.ico")


def init_manage_menu():
    manage_buttons_frame = ctk.CTkFrame(manage_menu,
                                        fg_color='transparent',
                                        )
    manage_buttons_frame.pack(side='top', fill='x')

    welcome_frame = ctk.CTkFrame(manage_menu,
                                 fg_color='transparent',
                                 )
    welcome_frame.pack()


    welcome_label_font = ctk.CTkFont(family="Golos Text", size=28)
    welcome_label = ctk.CTkLabel(welcome_frame,
                                 text="Добро пожаловать в\nМоя Библиотека!",
                                 font=welcome_label_font,
                                 fg_color="transparent",
                                 )
    welcome_label.pack(pady=(100, 0))


    info_frame = ctk.CTkFrame(manage_menu,
                              fg_color='transparent',
                              )
    info_frame.pack(side='bottom')

    info_label_font = ctk.CTkFont(family="Golos Text", size=12)
    info_label = ctk.CTkLabel(info_frame,
                              text="VKontakte: vk.com/rtsray\nTelegram: t.me/rtsray",
                              font=info_label_font,
                              fg_color='transparent',
                              text_color='#878787',
                              )
    info_label.pack(pady=(0, 48))


    buttons_font = ctk.CTkFont(family="Golos Text", size=13)
    button_libs = ctk.CTkButton(manage_buttons_frame,
                                   text="Библиотеки",
                                   fg_color="transparent",
                                   text_color="black",
                                   corner_radius=0,
                                   height=OBJECT_MM_HEIGHT,
                                   width=OBJECT_MM_WIDTH,
                                   hover_color="#dedede",
                                   font=buttons_font,
                                   border_width=1,
                                   border_color="#e0e0e0",
                                   command=lambda: check_libs(manage_menu, welcome_frame,
                                                              button_libs),
                                   )
    button_libs.pack(side='left')

    button_literature = ctk.CTkButton(manage_buttons_frame,
                                   text="Литература",
                                   fg_color="transparent",
                                   text_color="black",
                                   corner_radius=0,
                                   height=OBJECT_MM_HEIGHT,
                                   width=OBJECT_MM_WIDTH,
                                   hover_color="#dedede",
                                   font=buttons_font,
                                   border_width=1,
                                   border_color="#e0e0e0",
                                   )
    button_literature.pack(side='left')

    button_students = ctk.CTkButton(manage_buttons_frame,
                                   text="Ученики",
                                   fg_color="transparent",
                                   text_color="black",
                                   corner_radius=0,
                                   height=OBJECT_MM_HEIGHT,
                                   width=OBJECT_MM_WIDTH,
                                   hover_color="#dedede",
                                   font=buttons_font,
                                   border_width=1,
                                   border_color="#e0e0e0",
                                   )
    button_students.pack(side='left')

    button_help = ctk.CTkButton(manage_buttons_frame,
                                text="Помощь",
                                fg_color="transparent",
                                text_color="black",
                                corner_radius=0,
                                height=OBJECT_MM_HEIGHT,
                                width=OBJECT_MM_WIDTH,
                                hover_color="#dedede",
                                font=buttons_font,
                                border_width=1,
                                border_color="#e0e0e0",
                                )
    button_help.pack(side='left')

    button_profile = ctk.CTkButton(manage_buttons_frame,
                                   text="Профиль",
                                   fg_color="transparent",
                                   text_color="black",
                                   corner_radius=0,
                                   height=OBJECT_MM_HEIGHT,
                                   width=OBJECT_MM_WIDTH,
                                   hover_color="#dedede",
                                   font=buttons_font,
                                   border_width=1,
                                   border_color="#e0e0e0",
                                   )
    button_profile.pack(side='left')


init_manage_menu()

if __name__ == "__main__":
    manage_menu.mainloop()
