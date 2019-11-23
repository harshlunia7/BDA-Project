import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.update({'sex':'male','country':'Albania','year':1987,'age':'15-24 years'},{'$set':{'suicides_no':1,'population':22}})