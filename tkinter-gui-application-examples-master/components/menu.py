#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox

class MainMenu:
    """Main interface menu"""

    def __init__(self, master):
        """Initialization menu"""
        self.master = master # Superior
        self.root = master.root # Main window

        self.init_menu()

    def init_menu(self):
        """Load menu"""

        # Create a menu bar
        self.menubar = Menu(self.root)

        # Add a menu bar to the window
        self.root.config(menu=self.menubar)

        # File drop down menu
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.file_new)
        filemenu.add_command(label="turn on", command=self.file_open)
        filemenu.add_command(label="save", command=self.file_save)
        filemenu.add_command(label="Save as", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="drop out", command=self.root.quit)

        # User drop down menu
        usermenu = Menu(self.menubar, tearoff=0)
        usermenu.add_command(label="user list", command=self.master.open_user_list)
        usermenu.add_command(label="User added", command=self.master.open_user_add)
        usermenu.add_command(label="User details window", command=self.master.open_user_info)

        # Article drop-down menu
        articlemenu = Menu(self.menubar, tearoff=0)
        articlemenu.add_command(label="Article query", command=self.master.open_content_list)
        articlemenu.add_command(label="Article addition", command=self.master.open_content_add)
        articlemenu.add_command(label="Article statistics", command=self.master.open_content_count)

        # Data drop down menu
        datamenu = Menu(self.menubar, tearoff=0)
        datamenu.add_command(label="download", command=self.master.open_download)
        datamenu.add_command(label="Upload", command=self.master.open_upload)
        datamenu.add_command(label="Synchronize", command=self.master.open_synchronize)
        datamenu.add_command(label="Backup", command=self.master.open_backup)

        # Window drop down menu
        window_menu = Menu(self.menubar)
        window_menu.add_command(label="maximize")
        window_menu.add_command(label="minimize")
        window_menu.add_separator()
        window_menu.add_command(label="Window top", command=self.master.window_to_top)
        window_menu.add_command(label="Unpin", command=self.master.window_not_top)
        window_menu.add_separator()
        window_menu.add_command(label="Main interface", command=self.master.open_home)
        window_menu.add_command(label="Switch to: user")
        window_menu.add_command(label="Switch to: Article list")

        # Help drop down menu
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="welcome", command=self.help_about)
        helpmenu.add_command(label="Document", command=self.help_about)
        helpmenu.add_command(label="Copyright Notice", command=self.help_about)
        helpmenu.add_command(label="Privacy statement", command=self.help_about)
        helpmenu.add_separator()
        helpmenu.add_command(label="contact us", command=self.master.open_ontact)
        helpmenu.add_command(label="on", command=self.master.open_about)

        # Add a drop-down menu to the menu bar
        self.menubar.add_cascade(label="file", menu=filemenu)
        self.menubar.add_cascade(label="user", menu=usermenu)
        self.menubar.add_cascade(label="article", menu=articlemenu)
        self.menubar.add_cascade(label="data", menu=datamenu)
        self.menubar.add_cascade(label="window", menu=window_menu)
        self.menubar.add_cascade(label="help", menu=helpmenu)

    def file_open(self):
        messagebox.showinfo("turn on", "file-turn on！")  # Message prompt box

    def file_new(self):
        messagebox.showinfo("New", "file-New！")  # Message prompt box

    def file_save(self):
        messagebox.showinfo("save", "file-save！")  # Message prompt box

    def edit_cut(self):
        messagebox.showinfo("Cutting", "edit-Cutting！")  # Message prompt box

    def edit_copy(self):
        messagebox.showinfo("copy", "edit-copy！")  # Message prompt box

    def edit_paste(self):
        messagebox.showinfo("Paste", "edit-Paste！")  # Message prompt box

    def help_about(self):
        """on"""
        messagebox.showinfo(
            "on", "Author: doudoudzj \n verion 1.0 \n Thank you for your use！ \n doudoudzj@sina.com"
        )
