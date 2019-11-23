import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['suicide']
for x in mycol.find({'sex':'male','country':'Uzbekistan','year':2014,'age':'75+ years'}):
	print(x)