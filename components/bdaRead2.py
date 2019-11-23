import pymongo
import csv
def documentReturn():
	print('aa')
	myclient = pymongo.MongoClient('mongodb://localhost:27017/')
	mydb = myclient['suicideRate']
	mycol = mydb['suicideCollection']
	w = csv.writer(open('/Users/anish/Desktop/tkinter-gui-application-examples-master/components/Read.csv', 'a'))
	for x in mycol.find({'sex':'male','country':'Albania','year':1987,'age':'15-24 years'}):
		print(x)
		for key,val in x.items():
			print('aaasss')
			w.writerow([key,val])