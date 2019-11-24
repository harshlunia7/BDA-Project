
import tkinter as tk

from tkinter.tix import *




class myHome(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.init_page()

    def init_page(self):
        label = Label(self, text='Welcome \n To Suicide Data Analysis ')
        label.grid(row=0)
        label.config(font=("Courier", 30))


class myCreate(Frame):

    def __init__(self, parent=None):

        Frame.__init__(self, parent)
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
        self.init_page()


    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        Label(self,text = 'suicides/100k_pop').grid(row=6)
        Label(self,text = ' gdp_for_year ($) ').grid(row=7)
        Label(self,text = 'gdp_per_capita ($)').grid(row=8)
        button = tk.Button(self, text='Submit', width=25, command=self.createRecordDatabase)
        button.grid(row=9)
        e1 = Entry(self, textvariable=self.entrySex)
        e2 = Entry(self, textvariable=self.entryCountry)
        e3 = Entry(self, textvariable=self.entryYear)
        e4 = Entry(self, textvariable=self.entryAge)
        e5 = Entry(self, textvariable=self.suicides_no)
        e6 = Entry(self, textvariable=self.population)
        e7 = Entry(self, textvariable=self.suicidespop)
        e8 = Entry(self, textvariable=self.gdpforyear)
        e9 = Entry(self, textvariable=self.gdppercapita)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=7, column=1)
        e9.grid(row=8, column=1)

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


class myRead(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
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
        self.init_page()


    def readMyDatabase(self):
        self.entrySex3 = self.entrySex.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.entryAge3 = self.entryAge.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
        self.suicidespop3= self.suicidespop.get()
        self.gdpforyear3 = self.gdpforyear.get()
        self.gdppercapita3 = self.gdppercapita.get()
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaRead2.py", "w")
        t = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nw = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'w'))\nw.writerow(['_id',	'country','year','sex','age','suicides_no','population','suicides/100kpop','country-year','gdp_for_year($)','gdp_per_capita'])\nw = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))\nfor x in mycol.find({"
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
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        Label(self,text = 'suicides/100k_pop').grid(row=6)
        Label(self,text = ' gdp_for_year ($) ').grid(row=7)
        Label(self,text = 'gdp_per_capita ($)').grid(row=8)
        button = tk.Button(self, text='Submit', width=25, command=self.readMyDatabase)
        button.grid(row=9)
        e1 = Entry(self, textvariable=self.entrySex)
        e2 = Entry(self, textvariable=self.entryCountry)
        e3 = Entry(self, textvariable=self.entryYear)
        e4 = Entry(self, textvariable=self.entryAge)
        e5 = Entry(self, textvariable=self.suicides_no)
        e6 = Entry(self, textvariable=self.population)
        e7 = Entry(self, textvariable=self.suicidespop)
        e8 = Entry(self, textvariable=self.gdpforyear)
        e9 = Entry(self, textvariable=self.gdppercapita)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=7, column=1)
        e9.grid(row=8, column=1)


class myUpdate(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.suicides_no = StringVar()
        self.population = StringVar()
        self.init_page()

    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        button = tk.Button(self, text='Submit', width=25,command = self.updateMyDatabase)
        button.grid(row=6)
        e1 = Entry(self,textvariable = self.entrySex)
        e2 = Entry(self,textvariable = self.entryCountry)
        e3 = Entry(self,textvariable = self.entryYear)
        e4 = Entry(self,textvariable = self.entryAge)
        e5 = Entry(self,textvariable = self.suicides_no)
        e6 = Entry(self,textvariable =  self.population)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2,column=1)
        e4.grid(row=3,column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)

    def updateMyDatabase(self):
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaUpdate2.py", "w")
        self.entrySex3 = self.entrySex.get()
        self.entryAge3 = self.entryAge.get()
        self.entryCountry3 = self.entryCountry.get()
        self.entryYear3 = self.entryYear.get()
        self.suicides_no3 = self.suicides_no.get()
        self.population3 = self.population.get()
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
        if a == "":
            t1 = t1 + ")"
        else:
            t1 = t1 + a + "}})"
        file.write(t1)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaUpdate2.py")


class myDelete(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.root = parent
        self.entrySex = StringVar()
        self.entryCountry = StringVar()
        self.entryYear = StringVar()
        self.entryAge = StringVar()
        self.init_page()

    def deleteMyDatabase(self):
        self.entrySex4 = self.entrySex.get()
        self.entryAge4 = self.entryAge.get()
        self.entryCountry4 = self.entryCountry.get()
        self.entryYear4 = self.entryYear.get()
        file = open("/Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaDelete2.py", "w")
        t = "import pymongo\nimport csv\nmyclient = pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['suicideRate']\nmycol = mydb['suicideCollection']\nmycol.remove({"
        self.a = ""

        if self.entrySex4 != "-1":
            if self.a != "":
                self.a = self.a + ",'sex':'" + self.entrySex4 + "'"
            else:
                self.a = self.a + "'sex':'" + self.entrySex4 + "'"

        if self.entryCountry4 != "-1":
            if self.a != "":
                self.a = self.a + ",'country':'" + self.entryCountry4 + "'"
            else:
                self.a = self.a + "'country':'" + self.entryCountry4 + "'"
        if self.entryYear4 != "-1":
            if self.a != "":
                self.a = self.a + ",'year':" + self.entryYear4
            else:
                self.a = self.a + "'year':" + self.entryYear4
        if self.entryAge4 != "-1":
            if self.a != "":
                self.a = self.a + ",'age':'" + self.entryAge4 + "'"
            else:
                self.a = self.a + "'age':'" + self.entryAge4 + "'"

        t = t + self.a + "})"
        file.write(t)
        file.close()
        os.system("python3 /Users/anish/Desktop/tkinter-gui-application-examples-master/components/bdaDelete2.py")


    def init_page(self):
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
        button = tk.Button(self, text='Submit', width=25, command=self.deleteMyDatabase)
        button.grid(row=4)





