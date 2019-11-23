import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'w'))
w.writerow(['_id',	'country','year','sex','age','suicides_no','population','suicides/100kpop','country-year','gdp_for_year($)','gdp_per_capita','generation'])
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))
for x in mycol.find({'suicides/100k pop':'23'}):
	a=[]
	for key,val in x.items():
		a.append(val)
	w.writerow(a)