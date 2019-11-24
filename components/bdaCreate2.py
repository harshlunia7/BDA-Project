import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.insert({'country':'India','year':1998,'sex':'male','age':'21','suicides_no':'1000','population':'200033400','suicides/100k pop':'1212','gdp_for_year ($)':'193','gdp_per_capita ($)':'2323'})