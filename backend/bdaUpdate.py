import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['test']
mycol = mydb['suicide']
mycol.update({'sex':'male','country':'Uzbekistan','year':2014,'age':'75+ years'},{'$set':{'suicides_no':15}})