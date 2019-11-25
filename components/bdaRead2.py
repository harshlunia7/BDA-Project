import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'w'))
w.writerow(['_id',	'country','year','sex','age','suicides_no','population','suicides/100kpop','gdp_for_year($)','gdp_per_capita'])
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))
for x in mycol.find({'country':'Bangladesh','sex':'male'}):
	a=[]
	for key,val in x.items():
		a.append(val)
	w.writerow(a)