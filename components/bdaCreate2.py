import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.insert({'country':'Bangladesh','year':1998,'sex':'female','age':'21','suicides_no':'0','population':'0','suicides/100k pop':'0','gdp_for_year ($)':'0','gdp_per_capita ($)':'100'})