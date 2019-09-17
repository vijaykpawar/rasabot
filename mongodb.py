import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
teraDB = client["tera"]
intents = teraDB["intents"]
conversations = teraDB["conversations"]
from bson.son import SON
group_query = [{"$group": {"_id": "$name", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])}, {"$limit": 3}]
trends = []
group_by_results = intents.aggregate(group_query)
for cursor in group_by_results:
    res = intents.find({"name":cursor.get("_id")}).sort("confidence", -1).limit(1)
    trends.append(res[0].get("text"))

print(str(trends))

res = conversations.find({"events":{"event":"user"}})



