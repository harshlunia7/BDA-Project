file=open("/home/chethan/Documents/bdaRead.py","w")

t="import pymongo\nmyclient=pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['test']\nmycol = mydb['suicide']\nfor x in mycol.find({"
print('Enter choices')
country = input('Which country')
sex=input('Which sex')
year=input('Which year')
age=input('which age')
a=""
if sex!="-1":
	if a!="":
		a=a+",'sex':'"+sex+"'"
	else:
		a=a+"'sex':'"+sex+"'"

if country!="-1":
	if a!="":
		a=a+",'country':'"+country+"'"
	else:
		a=a+"'country':'"+country+"'"
if year!="-1":
	if a!="":
		a=a+",'year':"+year
	else:
		a=a+"'year':"+year
if age!="-1":
	if a!="":
		a=a+",'age':'"+age+"'"
	else:
		a=a+"'age':'"+age+"'"
t=t+a+"}):\n\tprint(x)"
file.write(t)
file.close()
