import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tera"]
mycol = mydb["intents"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)