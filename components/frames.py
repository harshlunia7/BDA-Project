#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk
import os
from tkinter import *

import lib.dbcontent as dbcontent
from components.bdaRead2 import documentReturn
from lib import global_variable
from lib.functions import treeview_sort_column
from pages import win_user_edit, win_user_info, winContentEdit, winContentInfo



class myHome(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        label = Label(self, text='Welcome \n Select One Of the Opeartions of CRUD ')
        label.grid(row=0)
        label.config(font=("Courier", 30))


class myCreate(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent  # 定义内部变量root
        self.init_page()

    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        e1 = Entry(self)
        e2 = Entry(self)
        e3 = Entry(self)
        e4 = Entry(self)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2,column=1)
        e4.grid(row=3,column=1)
        button = tk.Button(self, text='Submit', width=25)
        button.grid(row=5)
        ourMessage = 'This is our Message'
        messageVar = Message(self, text=ourMessage)
        messageVar.config(bg='lightgreen')
        messageVar.grid(row=6)


class myRead(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.init_page()

    def readMyDatabase(self):
        self.entrySex2 = self.entrySex.get()
        self.entryAge2 = self.entryAge.get()
        self.entryCountry2 = self.entryCountry.get()
        self.entryYear2 = self.entryYear.get()
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaRead2.py", "w")
        t = "import pymongo\nimport csv\ndef documentReturn():\n\tprint('aa')\n\tmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\n\tmydb = myclient['suicideRate']\n\tmycol = mydb['suicideCollection']\n\tw = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))\n\tfor x in mycol.find({"
        self.a = ""

        if self.entrySex2 != "-1":
            if self.a != "":
                self.a = self.a + ",'sex':'" + self.entrySex2 + "'"
            else:
                self.a = self.a + "'sex':'" + self.entrySex2 + "'"

        if self.entryCountry2 != "-1":
            if self.a != "":
                self.a = self.a + ",'country':'" + self.entryCountry2 + "'"
            else:
                self.a = self.a + "'country':'" + self.entryCountry2 + "'"
        if self.entryYear2 != "-1":
            if self.a != "":
                self.a = self.a + ",'year':" + self.entryYear2
            else:
                self.a = self.a + "'year':" + self.entryYear2
        if self.entryAge2 != "-1":
            if self.a != "":
                self.a = self.a + ",'age':'" + self.entryAge2 + "'"
            else:
                self.a = self.a + "'age':'" + self.entryAge2 + "'"

        t = t + self.a + "}):\n\t\tprint(x)\n\t\tfor key,val in x.items():\n\t\t\tprint('aaasss')\n\t\t\tw.writerow([key,val])"
        file.write(t)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaRead2.py")

        documentReturn()
     #   messageVar = Message(self, text=ourMessage)
      #  messageVar.config(bg='lightgreen')
       # messageVar.grid(row=6)
        '''if self.a!=" ":
            self.myText = documentReturn()
            Label(self,text = self.myText).grid(row=4)'''


    def init_page(self):
        #Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        e1 = Entry(self,textvariable = self.entrySex)
        e2 = Entry(self,textvariable = self.entryCountry)
        e3 = Entry(self,textvariable = self.entryYear)
        e4 = Entry(self,textvariable = self.entryAge)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        button = tk.Button(self, text='Submit', width=25, command=self.readMyDatabase)
        button.grid(row=4)



class myUpdate(Frame):

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
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        button = tk.Button(self, text='Submit', width=25)
        button.grid(row=6)
        e1 = Entry(self)
        e2 = Entry(self)
        e3 = Entry(self)
        e4 = Entry(self)
        e5 = Entry(self)
        e6 = Entry(self)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2,column=1)
        e4.grid(row=3,column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)




    def select(self, event):
        # event.widget获取Treeview对象，调用selection获取选择所有选中的
        slct = event.widget.selection()[0]
        self.selected_item = self.tree_view.item(slct)
        self.selected_name.set(self.selected_item["values"][1])
        # print("you clicked on ", self.selected_item)
        # print(self.selected_name)

    def info(self):
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


