
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
        self.e1 = Entry(self, textvariable=self.entrySex)
        self.e2 = Entry(self, textvariable=self.entryCountry)
        self.e3 = Entry(self, textvariable=self.entryYear)
        self.e4 = Entry(self, textvariable=self.entryAge)
        self.e5 = Entry(self, textvariable=self.suicides_no)
        self.e6 = Entry(self, textvariable=self.population)
        self.e7 = Entry(self, textvariable=self.suicidespop)
        self.e8 = Entry(self, textvariable=self.gdpforyear)
        self.e9 = Entry(self, textvariable=self.gdppercapita)
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
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        Label(self, text='suicides/100k_pop').grid(row=6)
        Label(self, text=' gdp_for_year ($) ').grid(row=7)
        Label(self, text='gdp_per_capita ($)').grid(row=8)
        button = tk.Button(self, text='Submit', width=25, command=self.readMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, textvariable=self.entrySex)
        self.e2 = Entry(self, textvariable=self.entryCountry)
        self.e3 = Entry(self, textvariable=self.entryYear)
        self.e4 = Entry(self, textvariable=self.entryAge)
        self.e5 = Entry(self, textvariable=self.suicides_no)
        self.e6 = Entry(self, textvariable=self.population)
        self.e7 = Entry(self, textvariable=self.suicidespop)
        self.e8 = Entry(self, textvariable=self.gdpforyear)
        self.e9 = Entry(self, textvariable=self.gdppercapita)
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
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        Label(self, text='suicides/100k_pop').grid(row=6)
        Label(self, text=' gdp_for_year ($) ').grid(row=7)
        Label(self, text='gdp_per_capita ($)').grid(row=8)
        button = tk.Button(self, text='Submit', width=25, command=self.updateMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, textvariable=self.entrySex)
        self.e2 = Entry(self, textvariable=self.entryCountry)
        self.e3 = Entry(self, textvariable=self.entryYear)
        self.e4 = Entry(self, textvariable=self.entryAge)
        self.e5 = Entry(self, textvariable=self.suicides_no)
        self.e6 = Entry(self, textvariable=self.population)
        self.e7 = Entry(self, textvariable=self.suicidespop)
        self.e8 = Entry(self, textvariable=self.gdpforyear)
        self.e9 = Entry(self, textvariable=self.gdppercapita)
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


class myDelete(Frame):

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


    def init_page(self):
        Label(self).grid(row=0, stick="w", pady=10)
        Label(self, text='Sex').grid(row=0)
        Label(self, text='Country').grid(row=1)
        Label(self, text='Year').grid(row=2)
        Label(self, text='Age').grid(row=3)
        Label(self, text='SuicideNumber').grid(row=4)
        Label(self, text='Population').grid(row=5)
        Label(self, text='suicides/100k_pop').grid(row=6)
        Label(self, text=' gdp_for_year ($) ').grid(row=7)
        Label(self, text='gdp_per_capita ($)').grid(row=8)
        button = tk.Button(self, text='Submit', width=25, command=self.deleteMyDatabase)
        button.grid(row=9)
        self.e1 = Entry(self, textvariable=self.entrySex)
        self.e2 = Entry(self, textvariable=self.entryCountry)
        self.e3 = Entry(self, textvariable=self.entryYear)
        self.e4 = Entry(self, textvariable=self.entryAge)
        self.e5 = Entry(self, textvariable=self.suicides_no)
        self.e6 = Entry(self, textvariable=self.population)
        self.e7 = Entry(self, textvariable=self.suicidespop)
        self.e8 = Entry(self, textvariable=self.gdpforyear)
        self.e9 = Entry(self, textvariable=self.gdppercapita)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.e8.grid(row=7, column=1)
        self.e9.grid(row=8, column=1)




