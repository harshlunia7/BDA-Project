import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.insert({'country':'Malaysia','year':1998,'sex':'female','age':'21','suicides_no':'1','population':'1','suicides/100k pop':'1','gdp_for_year ($)':'1','gdp_per_capita ($)':'1212'})