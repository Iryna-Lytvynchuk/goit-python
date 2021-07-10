from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://1234:1234@cluster0.wnt16.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = client.personal_assistent

'''
result_one = db.users.insert_one(
    {
        "name": "Irina",
        "surname": "Litv",
        "adress": "Vasylkiv",
        "note": ["car", "dog"],
        "tag":  ["car", "dog"],
        "email": "irina@meta.ua",
        "phone": ["0964772283", "0630542373"],
        "birthday": "13 03 1986",
    }
)

print(result_one.inserted_id)

result_many = db.users.insert_many(
    [
        {
        "name": "Serg",
        "surname": "Litv",
        "adress": "Vasylkiv",
        "note": ["car", "dog1"],
        "tag":  ["car", "dog1"],
        "email": "fhh@meta.ua",
        "phone": ["0964775283", "0650542373"],
        "birthday": "13 07 1984",
    },
        {
        "name": "Tymur",
        "surname": "Litv",
        "adress": "Vasylkiv",
        "note": ["car", "cat"],
        "tag":  ["car", "cat"],
        "email": "t@meta.ua",
        "phone": ["0964548974", "0862145689"],
        "birthday": "03 11 2011",
    },
    ]
)
print(result_many.inserted_ids)
'''

result = db.users.find_one({"_id": ObjectId("60e9c4ce88f8fb3cc3601934")})
print(result)


result_all = db.users.find({})
for i in result_all:
    print(i)