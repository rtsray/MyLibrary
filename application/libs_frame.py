import customtkinter as ctk

from constants import OBJECT_LIBS_HEIGHT, OBJECT_LIBS_WIDTH


def check_libs(master_frame, welcome_frame, button_libs):
    welcome_frame.destroy()
    button_libs.configure(fg_color="#dedede")


    scrollable_mylibs_frame = ctk.CTkScrollableFrame(master_frame,
                                                     corner_radius=30,
                                                     height=128,
                                                     width=256,
                                                     )
    scrollable_mylibs_frame.pack(pady=(32, 0))


    libs_frame = ctk.CTkFrame(master_frame,
                              fg_color='transparent',
                              )
    libs_frame.pack()

    buttons_font = ctk.CTkFont(family="Golos Text", size=12)
    add_lib = ctk.CTkButton(libs_frame,
                            text="Добавить",
                            command=None,
                            font=buttons_font,
                            height=OBJECT_LIBS_HEIGHT,
                            width=OBJECT_LIBS_WIDTH,
                            corner_radius=30,
                            fg_color='#2d82e3',
                            )
    add_lib.pack(side='left', pady=(16, 0), padx=(0, 8))

    del_lib = ctk.CTkButton(libs_frame,
                            text="Удалить",
                            command=None,
                            font=buttons_font,
                            height=OBJECT_LIBS_HEIGHT,
                            width=OBJECT_LIBS_WIDTH,
                            corner_radius=30,
                            fg_color='#2d82e3',
                            )
    del_lib.pack(side='left', pady=(16, 0), padx=(8, 0))