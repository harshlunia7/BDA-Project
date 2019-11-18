#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import (Button, Label, Frame, Entry, LabelFrame, StringVar, messagebox,
                     scrolledtext, ttk)

import lib.dbcontent as dbcontent
from lib import global_variable
from lib.functions import treeview_sort_column
from pages import win_user_edit, win_user_info, winContentEdit, winContentInfo


class myCreate(Frame):  # 继承Frame类
    """应用主界面"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.init_page()

    def init_page(self):
        Label(self, text="Create Function").pack()

class myRead(Frame):
    """文章添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.content_title = StringVar()
        self.content_textarea = None
        self.content_tag = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick="w", pady=10)

        lb1 = Label(self, text="title: ")
        lb1.grid(row=1, stick="w", pady=10)

        et1 = Entry(self, textvariable=self.content_title)
        et1.grid(row=1, column=1, stick="we")

        lb2 = Label(self, text="content: ")
        lb2.grid(row=2, stick="nw", pady=10)

        et2 = scrolledtext.ScrolledText(
            self,
            height=10,
            font=("Courier New", 13),
            fg="#333",
            borderwidth=1,
            highlightcolor="#ddd",
        )
        et2.grid(row=2, column=1, ipadx=10, stick="nswe")
        self.content_textarea = et2

        lb3 = Label(self, text="label: ")
        lb3.grid(row=3, stick="w", pady=10)

        et3 = Entry(self, textvariable=self.content_tag)
        et3.grid(row=3, column=1, columnspan=2, stick="we")

        bt1 = Button(self, text="Add to", command=self.do_add)
        bt1.grid(row=6, column=1, stick="e", pady=10)

    def do_add(self):
        """添加文章"""
        title = self.content_title.get()
        content = self.content_textarea.get(0.0, "end")
        tag = self.content_tag.get()
        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        res = dbcontent.content_add(username, title, content, tag)
        if res is True:
            self.content_title.set("")
            self.content_tag.set("")
            self.content_textarea.delete(1.0, "end")  # 清空
            self.content_textarea.update()
            messagebox.showinfo(title="success", message="Added successfully")
        else:
            messagebox.showinfo(title="error", message="add failed")


class myUpdate(Frame):
    """文章列表"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.list = []
        self.selected_item = None
        self.selected_name = StringVar()
        self.win_content_info = None
        self.win_content_edit = None
        self.init_page()

    def init_page(self):
        """加载控件"""

        username = str(global_variable.get_variable("CURRENT_USER_NAME"))
        self.list = dbcontent.content_list_by_username(username)

        head_frame = LabelFrame(self, text="Article operation")
        head_frame.grid(row=0, column=0, columnspan=2, sticky="nswe")
        Label(head_frame, textvariable=self.selected_name).pack()

        btn_info = Button(head_frame, text="Details", command=self.info)
        btn_info.pack(side="left")
        btn_edit = Button(head_frame, text="edit", command=self.edit)
        btn_edit.pack(side="left")
        btn_delete = Button(head_frame, text="delete", command=self.delete)
        btn_delete.pack(side="left")

        # 表格
        self.tree_view = ttk.Treeview(self, show="headings")

        self.tree_view["columns"] = ("id", "title", "content", "tag")
        # 列设置
        self.tree_view.column("id", width=100)
        # self.tree_view.column("title", width=100)
        # self.tree_view.column("content", width=100)
        # self.tree_view.column("tag", width=100)
        # 显示表头
        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("title", text="title")
        self.tree_view.heading("content", text="content")
        self.tree_view.heading("tag", text="label")

        # 插入数据
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["title"], item["content"], item["tag"]),
            )
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

        # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )

        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")

    def select(self, event):
        """选中"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
        """详情"""
        print("Details", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please choose first")
        else:
            if self.win_content_info is not None and hasattr(self.win_content_info.destroy, "__call__"):
                # if self.win_content_info and self.win_content_info.destroy:
                self.win_content_info.destroy()
            self.win_content_info = winContentInfo.Init(self.selected_item)
            # self.win_content_info = winAbout.Init()

    def edit(self):
        """编辑"""
        print("edit", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please choose first")
        else:
            if self.win_content_edit and self.win_content_edit.destroy:
                self.win_content_edit.destroy()
            self.win_content_edit = winContentEdit.Init(self.selected_item)

    def delete(self):
        """删除"""
        print(self.selected_item)
        messagebox.showinfo("delete?", self.selected_item)  # 弹出消息提示框


class myDelete(Frame):
    """文章统计"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self, text="Statistical interface").pack()



        self.tree_view.heading("id", text="ID")
        self.tree_view.heading("name", text="Name")
        self.tree_view.heading("password", text="password")
        self.tree_view.heading("op", text="operating")

        # 插入数据
        num = 1
        for item in self.list:
            self.tree_view.insert(
                "",
                num,
                text="",
                values=(item["id"], item["name"], item["password"], "Details"),
            )
        # 选中行
        self.tree_view.bind("<<TreeviewSelect>>", self.select)

       # 排序
        for col in self.tree_view["columns"]:  # 给所有标题加
            self.tree_view.heading(
                col,
                text=col,
                command=lambda _col=col: treeview_sort_column(
                    self.tree_view, _col, False
                ),
            )


        vbar = ttk.Scrollbar(self, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vbar.set)
        self.tree_view.grid(row=1, column=0, sticky="nsew")
        vbar.grid(row=1, column=1, sticky="ns")
        Label(self, text="Bottom action bar").grid(sticky="swe")

    def select(self, event):
        """选中"""
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])

    def info(self):
        """详情"""
        print("Details", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please choose first")
        else:
            if self.win_user_info is not None and (
                hasattr(self.win_user_info.destroy, "__call__")
            ):
                self.win_user_info.destroy()
            self.win_user_info = win_user_info.Init(self.selected_item)

    def edit(self):
        """用户编辑"""
        print("edit", self.selected_item)
        if self.selected_item is None:
            messagebox.showinfo("prompt", "Please choose first")
        else:
            if self.win_user_edit is not None and hasattr(
                self.win_user_edit.destroy, "__call__"
            ):
                self.win_user_edit.destroy()
            self.win_user_edit = win_user_edit.Init(self.selected_item)

    def delete(self):
        """用户删除"""
        print(self.selected_item)
        messagebox.showinfo("delete users?", self.selected_item)  # 弹出消息提示框

    def reset(self):
        """用户删除"""
        print("User delete")


class UserAddFrame(Frame):
    """用户添加"""

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.username = StringVar()
        self.password = StringVar()
        self.init_page()

    def init_page(self):
        """加载控件"""
        Label(self).grid(row=0, stick="w")

        Label(self, text="Account: ").grid(row=1, stick="w", pady=10)
        username = Entry(self, textvariable=self.username)
        username.grid(row=1, column=1, stick="e")

        Label(self, text="password: ").grid(row=2, stick="w", pady=10)
        password = Entry(self, textvariable=self.password, show="*")
        password.grid(row=2, column=1, stick="e")

        button_login = Button(self, text="Add to", command=self.do_add)
        button_login.grid(row=3, column=1, stick="w", pady=10)

    def do_add(self):
        """添加帐号"""
        # print(event)
        username = self.username.get()
        password = self.password.get()
        res = dbcontent.user_add(username, password)
        if res is True:
            self.username.set("")
            self.password.set("")
            messagebox.showinfo(title="success", message="Added successfully")
        else:
            messagebox.showinfo(title="error", message="Account already exists")
