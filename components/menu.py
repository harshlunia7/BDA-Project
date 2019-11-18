#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Menu, messagebox

from components import frames


class MainMenu:
    """Main interface menu"""

    def __init__(self, master):
        """Initialization menu"""
        self.master = master # Superior
        self.root = master.root # Main window
        self.page_frame = {
            "create": frames.myCreate,
            "read": frames.myRead,
            "update": frames.myUpdate,
            "delete": frames.myDelete
        }
        self.init_menu()

    def init_menu(self):
        """Load menu"""

        # Create a menu bar
        self.menubar = Menu(self.root)

        # Add a menu bar to the window
        self.root.config(menu=self.menubar)
        self.current_frame = None
        # File drop down menu
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Create", command=self.file_create)
        filemenu.add_command(label="Read", command=self.file_read)
        filemenu.add_command(label="Update", command=self.file_update)
        filemenu.add_command(label="Delete", command=self.file_delete)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        # Add a drop-down menu to the menu bar
        self.menubar.add_cascade(label="CRUD", menu=filemenu)

    def open_page(self, frame_name, title):
        """turn on/Replace the general function of the main interface"""
        self.root.title(title)
        # 先销毁之前frame
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def file_read(self):
        self.open_page("read", "Read")
        messagebox.showinfo("turn on", "file-turn on！")  # Message prompt box

    def file_create(self):
        self.open_page("create", "Create")
        messagebox.showinfo("New", "file-New！")  # Message prompt box

    def file_update(self):
        self.open_page("update", "Update")
        messagebox.showinfo("save", "file-save！")  # Message prompt box

    def file_delete(self):
        self.open_page("delete", "Delete")
        messagebox.showinfo("Cutting", "edit-Cutting！")  # Message prompt box

