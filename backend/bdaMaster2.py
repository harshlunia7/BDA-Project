file=open("/home/chethan/Documents/bdaUpdate.py","w")

t="import pymongo\nmyclient=pymongo.MongoClient('mongodb://localhost:27017/')\nmydb = myclient['test']\nmycol = mydb['suicide']\nmycol.update({"
print('Enter choices')
country=raw_input('Which country')
sex=raw_input('Which sex')
year=raw_input('Which year')
age=raw_input('which age')

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
t=t+a+"}"
a=",{'$set':{"
a=""
suicides_no=raw_input('Which suicides_no')
population=raw_input('which population')


if suicides_no!="-1":
	if a=="":
		a=a+",{'$set':{'suicides_no':"+suicides_no
	else:
		a=a+",'suicides_no':"+suicides_no

if population!="-1":
	if a=="":
		a=a+",{'$set':{'population':"+population
	else:
		a=a+",'population':"+population
if a=="":
	t=t+")"
else:
	t=t+a+"}})"
file.write(t)
file.close()
