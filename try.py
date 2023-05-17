from pymongo import MongoClient
from datetime import datetime, timedelta
from urllib.parse import quote_plus
from bson.objectid import ObjectId

username = "manojtomar326"
password = "Tomar@@##123"
cluster_url = "cluster0.ldghyxl.mongodb.net"

# Encode the username and password using quote_plus()
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Create the MongoDB Atlas connection string with the encoded credentials
connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_url}/test?retryWrites=true&w=majority"
# Connect to MongoDB Atlas


client = MongoClient(connection_string)

db = client['mydatabase']
collection = db['my_collection']
# Calculate the ObjectId for 24 hours ago
twenty_four_hours_ago = datetime.now() - timedelta(hours=24)

# Count the number of new objects added in data_dict within the last 24 hours
count = collection.count_documents({
    "data_dict": {"$exists": True, "$type": "array"},
    "data_dict": {"$elemMatch": {"timestamp": {"$gte": twenty_four_hours_ago}}}
})

print("Count of changed data_dict fields in the last 24 hours:", count)

# Iterate over each document in the collection
# for document in collection.find():
#     data_dict = document.get('data_dict', [])
    
#     # Iterate over each object in the data_dict array
#     for obj in data_dict:
#         # Add a timestamp field to each object with the current datetime
#         obj['timestamp'] = datetime.now()
    
#     # Update the document with the modified data_dict array
#     collection.update_one({'_id': document['_id']}, {'$set': {'data_dict': data_dict}})