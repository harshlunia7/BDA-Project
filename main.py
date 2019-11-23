#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""程序入口文件"""
import csv
import os
from tkinter import Tk

import pymongo

import lib.global_variable as glv
from pages import win_login, win_splah
from components.view import  MainPage

# Load global variable management module
glv.init_global_variable()
glv.set_variable("APP_NAME", "Application")
glv.set_variable("APP_PATH", os.path.dirname(__file__))
glv.set_variable("DATA_DIR", "data")


class App(Tk):
    """Application Class"""

    def __init__(self):
        win_splah.Splah()
        Tk.__init__(self)
        # Login Window
       # win_login.Login(self)
        MainPage(self)

        self.mainloop()



if __name__ == "__main__":
    App()
