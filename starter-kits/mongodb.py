# For full reference, visit:
# https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo

# client 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

# database
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

# collection
mycol = mydb["customers"]
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

# insertion
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# find
x = mycol.find_one()
print(x)

for x in mycol.find():
    print(x)
    
for x in mycol.find({},{ "address": 0 }):
    print(x)