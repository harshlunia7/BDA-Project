import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.remove({'sex':'male','country':'Albania','year':1987,'age':'15-24 years'})