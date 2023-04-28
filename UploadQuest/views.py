from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pymongo
from pymongo import MongoClient
from urllib.parse import quote_plus
# Create your views here.



# Replace <username>, <password>, and <cluster-url> with your MongoDB Atlas credentials
username = "priyam356"
password = "Tomar@@##123"
cluster_url = "cluster0.cawjk02.mongodb.net"

# Encode the username and password using quote_plus()
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Create the MongoDB Atlas connection string with the encoded credentials
connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_url}/test?retryWrites=true&w=majority"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)
db = client['mydatabase']  # Replace with your actual database name
collection = db['my_collection']  # Replace with your actual collection name

@csrf_exempt
def index(request):
    import csv
    from io import StringIO
    if request.method == 'POST' and request.FILES.get('csv_file'):
        if request.method == 'POST' and request.FILES.get('csv_file'):
            csv_file = request.FILES['csv_file']
            file_name = csv_file.name
            
            # Convert CSV to list of dictionaries
            csv_data = csv.DictReader(StringIO(csv_file.read().decode('utf-8')))
            data_list = [dict(row) for row in csv_data]
            
            # Transfer data to MongoDB using insert_many()
            if db is not None:
                result = collection.insert_many(data_list)
                # Print the IDs of the inserted documents
                print(result.inserted_ids)
            
            response_data = {'file_name': file_name}
            print(file_name)
            return JsonResponse(response_data)

    return render(request, "upload.html")