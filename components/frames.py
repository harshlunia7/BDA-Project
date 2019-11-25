
import tkinter as tk

from tkinter.tix import *

from tkinter import messagebox, ttk

import pymongo
from bson import SON
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

class myHome(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        label = Label(self,bg = 'cyan', text='Welcome \n To Suicide Data Analysis ')
        label.grid(row=0)
        label.config(font=("Courier", 30))


class myCreate(Frame):

    def __init__(self, parent=None):

        Frame.__init__(self, parent,bg='cyan')
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.suicides_no = StringVar()
        self.population = StringVar()
        self.suicidespop = StringVar()
        self.gdpforyear = StringVar()
        self.gdppercapita = StringVar()
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.e5 = Entry()
        self.e6 = Entry()
        self.e7 = Entry()
        self.e8 = Entry()
        self.e9 = Entry()
        self.init_page()


    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self,bg = 'cyan', text='Sex',font='Helvetica 18 bold').grid(row=0)
        Label(self,bg = 'cyan', text='Country',font='Helvetica 18 bold').grid(row=1)
        Label(self,bg = 'cyan', text='Year',font='Helvetica 18 bold').grid(row=2)
        Label(self,bg = 'cyan', text='Age',font='Helvetica 18 bold').grid(row=3)
        Label(self,bg = 'cyan', text='SuicideNumber',font='Helvetica 18 bold').grid(row=4)
        Label(self,bg = 'cyan', text='Population',font='Helvetica 18 bold').grid(row=5)
        Label(self,bg = 'cyan',text = 'suicides/100k_pop',font='Helvetica 18 bold').grid(row=6)
        Label(self,bg = 'cyan',text = ' gdp_for_year ($) ',font='Helvetica 18 bold').grid(row=7)
        Label(self,bg = 'cyan',text = 'gdp_per_capita ($)',font='Helvetica 18 bold').grid(row=8)
        ttk.Style().configure('green/black.TLabel', foreground='green', background='black')

        button = tk.Button(self, text='Submit',highlightbackground='#3E4149', width=25, command=self.createRecordDatabase)
        button.grid(row=9)
        self.e1 = Entry(self,bg='cyan', textvariable=self.entrySex)
        self.e2 = Entry(self,bg='cyan', textvariable=self.entryCountry)
        self.e3 = Entry(self,bg='cyan', textvariable=self.entryYear)
        self.e4 = Entry(self,bg='cyan', textvariable=self.entryAge)
        self.e5 = Entry(self,bg='cyan', textvariable=self.suicides_no)
        self.e6 = Entry(self,bg='cyan', textvariable=self.population)
        self.e7 = Entry(self,bg='cyan', textvariable=self.suicidespop)
        self.e8 = Entry(self,bg='cyan', textvariable=self.gdpforyear)
        self.e9 = Entry(self,bg='cyan', textvariable=self.gdppercapita)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)

    def createRecordDatabase(self):
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaCreate2.py", "w")
        self.entrySex3 = self.entrySex.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.entryAge3 = self.entryAge.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
        self.suicidespop3= self.suicidespop.get()
        self.gdpforyear3 = self.gdpforyear.get()
        self.gdppercapita3 = self.gdppercapita.get()

        self.e1.delete(0,'end')
        self.e2.delete(0,'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')
        t1 = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nmycol.insert({"

        a = ""


        if self.entryCountry3 != "-1":
             if a != "":
                a = a + ",'country':'" + self.entryCountry3 + "'"
             else:
                a = a + "'country':'" + self.entryCountry3 + "'"

        if self.entryYear3 != "-1":
             if a != "":
                a = a + ",'year':" + self.entryYear3
             else:
                a = a + "'year':" + self.entryYear3
        if self.entrySex3 != "-1":
             if a != "":
                a = a + ",'sex':'" + self.entrySex3 + "'"
             else:
                a = a + "'sex':'" + self.entrySex3 + "'"


        if self.entryAge3 != "-1":
             if a != "":
                a = a + ",'age':'" + self.entryAge3 + "'"
             else:
                a = a + "'age':'" + self.entryAge3 + "'"
        if self.suicides_no3 != "-1":
            if a != "":
                a = a + ",'suicides_no':'" + self.suicides_no3 + "'"
            else:
                a = a + "'suicides_no':'" + self.suicides_no3 + "'"
        if self.population3 != "-1":
            if a != "":
                a = a + ",'population':'" + self.population3 + "'"
            else:
                a = a + "'population':'" + self.population3 + "'"
        if self.suicidespop3 != "-1":
            if a != "":
                a = a + ",'suicides/100k pop':'" + self.suicidespop3 + "'"
            else:
                a = a + "'suicides/100k pop':'" + self.suicidespop3 + "'"
        if self.gdpforyear3 != "-1":
            if a != "":
                a = a + ",'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
            else:
                a = a + "'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
        if self.gdppercapita3 != "-1":
            if a != "":
                a = a + ",'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"
            else:
                a = a + "'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"

        t1 = t1 + a + "})"
        file.write(t1)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaCreate2.py")

        messagebox.showinfo("Create", "Record Created Successfully")


class myRead(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent,bg='cyan')
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.suicides_no = StringVar()
        self.population = StringVar()
        self.suicidespop = StringVar()
        self.gdpforyear = StringVar()
        self.gdppercapita = StringVar()
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.e5 = Entry()
        self.e6 = Entry()
        self.e7 = Entry()
        self.e8 = Entry()
        self.e9 = Entry()
        self.init_page()


    def readMyDatabase(self):
        self.entrySex3 = self.entrySex.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.entryAge3 = self.entryAge.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
        self.suicidespop3 = self.suicidespop.get()
        self.gdpforyear3 = self.gdpforyear.get()
        self.gdppercapita3 = self.gdppercapita.get()

        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaRead2.py", "w")
        t = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nw = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'w'))\nw.writerow(['_id',	'country','year','sex','age','suicides_no','population','suicides/100kpop','gdp_for_year($)','gdp_per_capita'])\nw = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))\nfor x in mycol.find({"
        a = ""

        if self.entryCountry3 != "-1":
            if a != "":
                a = a + ",'country':'" + self.entryCountry3 + "'"
            else:
                a = a + "'country':'" + self.entryCountry3 + "'"

        if self.entryYear3 != "-1":
            if a != "":
                a = a + ",'year':" + self.entryYear3
            else:
                a = a + "'year':" + self.entryYear3
        if self.entrySex3 != "-1":
            if a != "":
                a = a + ",'sex':'" + self.entrySex3 + "'"
            else:
                a = a + "'sex':'" + self.entrySex3 + "'"

        if self.entryAge3 != "-1":
            if a != "":
                a = a + ",'age':'" + self.entryAge3 + "'"
            else:
                a = a + "'age':'" + self.entryAge3 + "'"
        if self.suicides_no3 != "-1":
            if a != "":
                a = a + ",'suicides_no':'" + self.suicides_no3 + "'"
            else:
                a = a + "'suicides_no':'" + self.suicides_no3 + "'"
        if self.population3 != "-1":
            if a != "":
                a = a + ",'population':'" + self.population3 + "'"
            else:
                a = a + "'population':'" + self.population3 + "'"
        if self.suicidespop3 != "-1":
            if a != "":
                a = a + ",'suicides/100k pop':'" + self.suicidespop3 + "'"
            else:
                a = a + "'suicides/100k pop':'" + self.suicidespop3 + "'"
        if self.gdpforyear3 != "-1":
            if a != "":
                a = a + ",'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
            else:
                a = a + "'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
        if self.gdppercapita3 != "-1":
            if a != "":
                a = a + ",'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"
            else:
                a = a + "'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"

        t = t + a + "}):\n\ta=[]\n\tfor key,val in x.items():\n\t\ta.append(val)\n\tw.writerow(a)"
        file.write(t)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaRead2.py")

        os.system("open /Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv")


    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, bg='cyan', text='Sex', font='Helvetica 18 bold').grid(row=0)
        Label(self, bg='cyan', text='Country', font='Helvetica 18 bold').grid(row=1)
        Label(self, bg='cyan', text='Year', font='Helvetica 18 bold').grid(row=2)
        Label(self, bg='cyan', text='Age', font='Helvetica 18 bold').grid(row=3)
        Label(self, bg='cyan', text='SuicideNumber', font='Helvetica 18 bold').grid(row=4)
        Label(self, bg='cyan', text='Population', font='Helvetica 18 bold').grid(row=5)
        Label(self, bg='cyan', text='suicides/100k_pop', font='Helvetica 18 bold').grid(row=6)
        Label(self, bg='cyan', text=' gdp_for_year ($) ', font='Helvetica 18 bold').grid(row=7)
        Label(self, bg='cyan', text='gdp_per_capita ($)', font='Helvetica 18 bold').grid(row=8)
        button = tk.Button(self, text='Submit',highlightbackground='#3E4149', width=25, command=self.readMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, bg='cyan', textvariable=self.entrySex)
        self.e2 = Entry(self, bg='cyan', textvariable=self.entryCountry)
        self.e3 = Entry(self, bg='cyan', textvariable=self.entryYear)
        self.e4 = Entry(self, bg='cyan', textvariable=self.entryAge)
        self.e5 = Entry(self, bg='cyan', textvariable=self.suicides_no)
        self.e6 = Entry(self, bg='cyan', textvariable=self.population)
        self.e7 = Entry(self, bg='cyan', textvariable=self.suicidespop)
        self.e8 = Entry(self, bg='cyan', textvariable=self.gdpforyear)
        self.e9 = Entry(self, bg='cyan', textvariable=self.gdppercapita)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)


class myUpdate(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent,bg='cyan')
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.suicides_no = StringVar()
        self.population = StringVar()
        self.suicidespop = StringVar()
        self.gdpforyear = StringVar()
        self.gdppercapita = StringVar()
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.e5 = Entry()
        self.e6 = Entry()
        self.e7 = Entry()
        self.e8 = Entry()
        self.e9 = Entry()
        self.init_page()

    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, bg='cyan', text='Sex', font='Helvetica 18 bold').grid(row=0)
        Label(self, bg='cyan', text='Country', font='Helvetica 18 bold').grid(row=1)
        Label(self, bg='cyan', text='Year', font='Helvetica 18 bold').grid(row=2)
        Label(self, bg='cyan', text='Age', font='Helvetica 18 bold').grid(row=3)
        Label(self, bg='cyan', text='SuicideNumber', font='Helvetica 18 bold').grid(row=4)
        Label(self, bg='cyan', text='Population', font='Helvetica 18 bold').grid(row=5)
        Label(self, bg='cyan', text='suicides/100k_pop', font='Helvetica 18 bold').grid(row=6)
        Label(self, bg='cyan', text=' gdp_for_year ($) ', font='Helvetica 18 bold').grid(row=7)
        Label(self, bg='cyan', text='gdp_per_capita ($)', font='Helvetica 18 bold').grid(row=8)
        button = tk.Button(self, text='Submit',highlightbackground='#3E4149', width=25, command=self.updateMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, bg='cyan', textvariable=self.entrySex)
        self.e2 = Entry(self, bg='cyan', textvariable=self.entryCountry)
        self.e3 = Entry(self, bg='cyan', textvariable=self.entryYear)
        self.e4 = Entry(self, bg='cyan', textvariable=self.entryAge)
        self.e5 = Entry(self, bg='cyan', textvariable=self.suicides_no)
        self.e6 = Entry(self, bg='cyan', textvariable=self.population)
        self.e7 = Entry(self, bg='cyan', textvariable=self.suicidespop)
        self.e8 = Entry(self, bg='cyan', textvariable=self.gdpforyear)
        self.e9 = Entry(self, bg='cyan', textvariable=self.gdppercapita)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)


    def updateMyDatabase(self):
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaUpdate2.py", "w")
        self.entrySex3 = self.entrySex.get()
        self.entryAge3 = self.entryAge.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
        self.suicidespop3 = self.suicidespop.get()
        self.gdpforyear3 = self.gdpforyear.get()
        self.gdppercapita3 = self.gdppercapita.get()

        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')
        t1 = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nmycol.update({"

        a = ""
        if self.entrySex3 != "-1":
            if a != "":
                a = a + ",'sex':'" + self.entrySex3 + "'"
            else:
                a = a + "'sex':'" + self.entrySex3 + "'"

        if self.entryCountry3 != "-1":
            if a != "":
                a = a + ",'country':'" + self.entryCountry3 + "'"
            else:
                a = a + "'country':'" + self.entryCountry3 + "'"
        if self.entryYear3 != "-1":
            if a != "":
                a = a + ",'year':" + self.entryYear3
            else:
                a = a + "'year':" + self.entryYear3
        if self.entryAge3  != "-1":
            if a != "":
                a = a + ",'age':'" + self.entryAge3  + "'"
            else:
                a = a + "'age':'" + self.entryAge3  + "'"
        t1 = t1 + a + "}"
        a = ",{'$set':{"
        a = ""


        if self.suicides_no3 != "-1":
            if a == "":
                a = a + ",{'$set':{'suicides_no':" + self.suicides_no3
            else:
                a = a + ",'suicides_no':" + self.suicides_no3

        if self.population3 != "-1":
            if a == "":
                a = a + ",{'$set':{'population':" + self.population3
            else:
                a = a + ",'population':" + self.population3
        if self.suicidespop3 != "-1":
            if a != "":
                a = a + ",'suicides/100k pop':'" + self.suicidespop3 + "'"
            else:
                a = a + "'suicides/100k pop':'" + self.suicidespop3 + "'"
        if self.gdpforyear3 != "-1":
            if a != "":
                a = a + ",'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
            else:
                a = a + "'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
        if self.gdppercapita3 != "-1":
            if a != "":
                a = a + ",'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"
            else:
                a = a + "'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"
        if a == "":
            t1 = t1 + ")"
        else:
            t1 = t1 + a + "}})"
        file.write(t1)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaUpdate2.py")

        messagebox.showinfo("Update", "Record Updated Successfully")


class myDelete(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent,bg='cyan')
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.suicides_no = StringVar()
        self.population = StringVar()
        self.suicidespop = StringVar()
        self.gdpforyear = StringVar()
        self.gdppercapita = StringVar()
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.e5 = Entry()
        self.e6 = Entry()
        self.e7 = Entry()
        self.e8 = Entry()
        self.e9 = Entry()
        self.init_page()


    def deleteMyDatabase(self):
        self.entrySex3 = self.entrySex.get()
        self.entryAge3 = self.entryAge.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
        self.suicidespop3 = self.suicidespop.get()
        self.gdpforyear3 = self.gdpforyear.get()
        self.gdppercapita3 = self.gdppercapita.get()

        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')


        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaDelete2.py", "w")
        t = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nmycol.remove({"
        self.a = ""

        if self.entrySex3 != "-1":
            if self.a != "":
                self.a = self.a + ",'sex':'" + self.entrySex3 + "'"
            else:
                self.a = self.a + "'sex':'" + self.entrySex3 + "'"

        if self.entryCountry3 != "-1":
            if self.a != "":
                self.a = self.a + ",'country':'" + self.entryCountry3 + "'"
            else:
                self.a = self.a + "'country':'" + self.entryCountry3 + "'"
        if self.entryYear3 != "-1":
            if self.a != "":
                self.a = self.a + ",'year':" + self.entryYear3
            else:
                self.a = self.a + "'year':" + self.entryYear3
        if self.entryAge3 != "-1":
            if self.a != "":
                self.a = self.a + ",'age':'" + self.entryAge3 + "'"
            else:
                self.a = self.a + "'age':'" + self.entryAge3 + "'"
        if self.suicides_no3 != "-1":
            if self.a == "":
                self.a = self.a + ",{'$set':{'suicides_no':" + self.suicides_no3
            else:
                self.a = self.a + ",'suicides_no':" + self.suicides_no3

        if self.population3 != "-1":
            if self.a == "":
                self.a = self.a + ",{'$set':{'population':" + self.population3
            else:
                self.a = self.a + ",'population':" + self.population3
        if self.suicidespop3 != "-1":
            if self.a != "":
                self.a = self.a + ",'suicides/100k pop':'" + self.suicidespop3 + "'"
            else:
                self.a = self.a + "'suicides/100k pop':'" + self.suicidespop3 + "'"
        if self.gdpforyear3 != "-1":
            if self.a != "":
                self.a = self.a + ",'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
            else:
                self.a = self.a + "'gdp_for_year ($)':'" + self.gdpforyear3 + "'"
        if self.gdppercapita3 != "-1":
            if self.a != "":
                self.a = self.a + ",'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"
            else:
                self.a = self.a + "'gdp_per_capita ($)':'" + self.gdppercapita3 + "'"


        t = t + self.a + "})"
        file.write(t)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaDelete2.py")

        messagebox.showinfo("Delete", "Record Deleted Successfully")



    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, bg='cyan', text='Sex', font='Helvetica 18 bold').grid(row=0)
        Label(self, bg='cyan', text='Country', font='Helvetica 18 bold').grid(row=1)
        Label(self, bg='cyan', text='Year', font='Helvetica 18 bold').grid(row=2)
        Label(self, bg='cyan', text='Age', font='Helvetica 18 bold').grid(row=3)
        Label(self, bg='cyan', text='SuicideNumber', font='Helvetica 18 bold').grid(row=4)
        Label(self, bg='cyan', text='Population', font='Helvetica 18 bold').grid(row=5)
        Label(self, bg='cyan', text='suicides/100k_pop', font='Helvetica 18 bold').grid(row=6)
        Label(self, bg='cyan', text=' gdp_for_year ($) ', font='Helvetica 18 bold').grid(row=7)
        Label(self, bg='cyan', text='gdp_per_capita ($)', font='Helvetica 18 bold').grid(row=8)
        button = tk.Button(self, text='Submit',highlightbackground='#3E4149', width=25, command=self.deleteMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, bg='cyan', textvariable=self.entrySex)
        self.e2 = Entry(self, bg='cyan', textvariable=self.entryCountry)
        self.e3 = Entry(self, bg='cyan', textvariable=self.entryYear)
        self.e4 = Entry(self, bg='cyan', textvariable=self.entryAge)
        self.e5 = Entry(self, bg='cyan', textvariable=self.suicides_no)
        self.e6 = Entry(self, bg='cyan', textvariable=self.population)
        self.e7 = Entry(self, bg='cyan', textvariable=self.suicidespop)
        self.e8 = Entry(self, bg='cyan', textvariable=self.gdpforyear)
        self.e9 = Entry(self, bg='cyan', textvariable=self.gdppercapita)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)


class myGraphs(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent,bg='cyan')
        self.root = parent
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.mydb = self.myclient['suicideRate']
        self.mycol = self.mydb['suicideCollection']
        self.init_page()

    def create_1(self):
        mydata = self.mycol.aggregate([
            {"$group": {
                "_id": "$year",
                "total_suicide": {"$sum": "$suicides_no"}
            }},
            {"$sort": SON([("_id", 1)])}
        ])

        df = pd.DataFrame(list(mydata))
        df.reset_index(level=0, inplace=True)
        print(df.tail(5))
        df = df.rename(columns={'_id': 'Year', 'total_suicide': 'SuicidesNo'})
        df.drop(df.index[-1], inplace=True)
        df.plot(x='Year', y='SuicidesNo', kind='line')
        plt.show()


    def create_2(self):
        df = pd.DataFrame(list(self.mycol.find({})))
        df.reset_index(level=0, inplace=True)
        sns.barplot(x='sex', y='suicides_no', hue='age', data=df)
        plt.show()

    def create_3(self):
        mydata_male = self.mycol.aggregate([
            {"$match": {"sex": "male"}},
            {"$group": {
                "_id": "$year",
                "total_suicide": {"$sum": "$suicides_no"}
            }},
            {"$sort": SON([("_id", 1)])}
        ])
        df_male = pd.DataFrame(list(mydata_male))
        df_male.reset_index(level=0, inplace=True)
        df_male.drop(df_male.index[-1], inplace=True)
        df_male = df_male.rename(columns={'_id': 'Year', 'total_suicide': 'SuicidesNo'})

        mydata_female = self.mycol.aggregate([
            {"$match": {"sex": "female"}},
            {"$group": {
                "_id": "$year",
                "total_suicide": {"$sum": "$suicides_no"}
            }},
            {"$sort": SON([("_id", 1)])}
        ])
        df_female = pd.DataFrame(list(mydata_female))
        df_female.reset_index(level=0, inplace=True)
        df_female.drop(df_female.index[-1], inplace=True)
        df_female = df_female.rename(columns={'_id': 'Year', 'total_suicide': 'SuicidesNo'})

        male_plot = sns.lineplot(x='Year', y='SuicidesNo', data=df_male)
        female_plot = sns.lineplot(x='Year', y='SuicidesNo', data=df_female)
        plt.legend(['males', 'females'])

        plt.show()

    def create_4(self):
        mydata = self.mycol.aggregate([
            {"$group": {
                "_id": "$country",
                "total_suicide": {"$sum": "$suicides_no"}
            }},
            {"$sort": SON([("total_suicide", -1)])}
        ])
        df = pd.DataFrame(list(mydata))
        df.reset_index(level=0, inplace=True)
        df = df.rename(columns={'_id': 'Country', 'total_suicide': 'SuicidesNo'})
        sns.barplot(y='Country', x='SuicidesNo', data=df.head(15))
        plt.show()

    def create_5(self):
        df = pd.DataFrame(self.mycol.find({}, {'_id': 0}))
        df = df.rename(
            columns={'country': 'Country', 'year': 'Year', 'sex': 'Gender', 'age': 'Age', 'suicides_no': 'SuicidesNo',
                     'population': 'Population', 'suicides/100k pop': 'Suicides100kPop',
                     ' gdp_for_year ($) ': 'GdpForYearMoney', 'gdp_per_capita ($)': 'GdpPerCapitalMoney'})
        df.reset_index(level=0, inplace=True)
        sns.heatmap(df.corr(), cmap='YlGnBu', annot=True)
        plt.show()

    def init_page(self):
        Label(self, text='lineplot: for total suicides over years 1985 - 2015').grid(row=0, column=1)
        Label(self, text='barplot for gender and suicide_no with age').grid(row=1, column=1)
        Label(self, text='lineplot of male and female suicides over the years 1985 to 2015 separately').grid(row=2,
                                                                                                             column=1)
        Label(self, text='barplot where country wise total suicides taken place in years 1985 - 2016').grid(row=3,
                                                                                                            column=1)
        Label(self, text='heatmap of correlation matrix').grid(row=4, column=1)
        b1 = tk.Button(self, text='Graph 1', command=self.create_1)
        b2 = tk.Button(self, text='Graph 2', command=self.create_2)
        b3 = tk.Button(self, text='Graph 3', command=self.create_3)
        b4 = tk.Button(self, text='Graph 4', command=self.create_4)
        b5 = tk.Button(self, text='Graph 5', command=self.create_5)
        b1.grid(row=0)
        b2.grid(row=1)
        b3.grid(row=2)
        b4.grid(row=3)
        b5.grid(row=4)


