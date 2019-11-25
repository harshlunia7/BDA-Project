import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.insert({'country':'Malaysia','year':1998,'sex':'male','age':'22','suicides_no':'22','population':'22','suicides/100k pop':'22','gdp_for_year ($)':'22','gdp_per_capita ($)':'22'})