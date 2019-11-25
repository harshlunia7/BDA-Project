import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'w'))
w.writerow(['_id',	'country','year','sex','age','suicides_no','population','suicides/100kpop','gdp_for_year($)','gdp_per_capita'])
w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))
for x in mycol.find({'country':'Singapore','year':1998,'sex':'male','age':'21','suicides_no':'0','population':'0','suicides/100k pop':'0','gdp_for_year ($)':'0','gdp_per_capita ($)':'0'}):
	a=[]
	for key,val in x.items():
		a.append(val)
	w.writerow(a)