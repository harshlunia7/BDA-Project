import pymongo
import csv
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['suicideRate']
mycol = mydb['suicideCollection']
mycol.insert({'country':'Australia','year':2020,'sex':'male','age':'15-24 years','suicides_no':'10','population':'100000','suicides/100k pop':'23','country-year':'Australia 2020','gdp_for_year ($)':'546578','gdp_per_capita ($)':'54','generation':'silent'})