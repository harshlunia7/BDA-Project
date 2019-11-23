#!/usr/bin/env python3x
# -*- coding: UTF-8 -*-

from tkinter import Toplevel, Label, Message
from components import frames, menu
from lib.functions import set_window_center
from pages import winAbout


class MainPage():
    """主界面"""

    def __init__(self, master=None):
        self.root = master # 主窗口
        set_window_center(self.root, 800, 600)
        menu.MainMenu(self) # Use self to pass the main window and the main window operation function
        # initializationFrames
        self.current_frame = None
        self.page_frame = {
            "home":frames.myHome,
            "create": frames.myCreate,
            "read": frames.myRead,
            "update": frames.myUpdate,
            "delete": frames.myDelete
        }
        self.open_home()
        self.win_about = None

    def open_page(self, frame_name, title):
        """turn on/Replace the general function of the main interface"""
        self.root.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def open_home(self):
        """应用主界面"""
        self.open_page("home", "CRUD Operations")

    def open_content_add(self):
        """文章添加"""
        self.open_page("content_add", "Article addition")

    def open_content_list(self):
        """文章列表"""
        self.open_page("content_list", "Article query")

    def open_content_count(self):
        """文章统计"""
        self.open_page("count", "Article statistics")

    def open_ontact(self):
        """联系我们"""
        self.open_page("contact", "contact us")

    def open_user_info(self):
        """用户详情"""
        page = Toplevel()
        page.title("User details")
        page.resizable(False, False)
        set_window_center(page, 200, 150)

        # Label(page).grid(row=0, stick="w", pady=2)

        Label(page, text="Name: ").grid(row=1, stick="w", pady=2)
        Label(page, text="administrator").grid(row=1, column=1, stick="e")

        Label(page, text="Account: ").grid(row=2, stick="w", pady=2)
        Label(page, text="admin").grid(row=2, column=1, stick="e")

        Label(page, text="password: ").grid(row=3, stick="w", pady=2)
        Label(page, text="admin").grid(row=3, column=1, stick="e")

    def open_user_list(self):
        """用户列表"""
        self.open_page("user_list", "user list")
        # self.page_frame['user_list'].init_data()

    def open_user_add(self):
        """用户添加"""
        self.open_page("user_add", "User added")

    def open_download(self):
        """下载窗口"""
        root = Toplevel()
        root.title("Download management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello hello hello hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-ups, with separate window properties.", width=150)
        msg.pack()

    def open_upload(self):
        """上传管理"""
        root = Toplevel()
        root.title("Upload management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello hello hello hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-ups, with separate window properties.", width=150)
        msg.pack()

    def open_synchronize(self):
        """同步管理"""
        root = Toplevel()
        root.title("Synchronous management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello hello hello hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-ups, with separate window properties.", width=150)
        msg.pack()

    def open_backup(self):
        """备份管理"""
        root = Toplevel()
        root.title("Backup management")
        set_window_center(root, 400, 400)
        msg = Label(root, text="Hello hello hello hello")
        msg.pack(expand="yes", fill="both")
        msg = Message(root, text="Similar to pop-ups, with separate window properties.", width=150)
        msg.pack()

    def open_about(self):
        """关于窗口"""
        if self.win_about and self.win_about.destroy:
            self.win_about.destroy()
        self.win_about = winAbout.Init()

    def window_to_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', True)

    def window_not_top(self):
        """窗口置顶"""
        self.root.attributes('-topmost', False)
