from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from pymongo import MongoClient
from urllib.parse import quote_plus
import csv
import pymongo
from io import StringIO
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.


# Replace <username>, <password>, and <cluster-url> with your MongoDB Atlas credentials
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
db = client['mydatabase']  # Replace with your actual database name
collection = db['my_collection']  # Replace with your actual collection name

@csrf_exempt
def index(request):
    from time import sleep
    if request.user.is_anonymous:
        print("redirecting to login")
        return redirect('/login')
    update =0
    data_list = []

    if request.method == 'POST' and request.FILES.get('csv_file'):
        # Assuming the CSV file is uploaded through a Django form, and its field name is 'csv_file'
        csv_file = request.FILES['csv_file']

        # Convert CSV to list of dictionaries, and skip any key-value pairs where the key is an empty string
        csv_data = csv.DictReader(StringIO(csv_file.read().decode('utf-8')))
        data_list = []
        for row in csv_data:
            row = {str(k): v for k, v in row.items() if k != ''}
            data_list.append(row)


        # Find the document with the highest id value, and project only the id field
        result = collection.aggregate([
            {'$project': {
                'id_numeric': {'$convert': {'input': '$id', 'to': 'int'}}
            }},
            {'$sort': {'id_numeric': -1}},
            {'$limit': 1},
            {'$project': {'_id': 0, 'highest_id': '$id_numeric'}}
        ])
        record_orgid = result.next()['highest_id']
        record_orgid += 1

        for record in data_list:
            record['totalProfiles'] = 0
            record['email'] = 'none'
            record['status'] = 'pending'
            record['id'] = str(record_orgid)
            record_orgid += 1

        # Insert data into MongoDB collection
        if db is not None:
            result = collection.insert_many(data_list)

        response_data = {'file_name': csv_file.name}
        return JsonResponse(response_data)

    return render(request, "templates/upload.html")

def loginuser(request):
    if request.method == "POST":
        user = request.POST.get("username")
        passw = request.POST.get("password")

        print(user,passw)
        user = authenticate(username=user, password=passw)
        if user is not None:
            # A backend authenticated the credentials
            print("User is not none")
            login(request,user)
            return redirect('/')

        else:
            print("The password is incorrect")
            return redirect('/login')

    if request.user.is_anonymous:
        return render(request,"templates/login.html")
    else:
        return redirect('/')

def logoutuser(request):
    logout(request)
    cache.clear()
    return redirect('/')

def account(request):
    if request.user.is_anonymous:
        return redirect('/')
    users_collection = db["users"]
    usern = request.user
    user = users_collection.find_one({"username": usern})
    if user:
        email = user.get("email")
        print(email)
        context = {'username':usern,'email':'not found'}
        return render(request,"templates/account.html",context)
    
def clear_cache(request):
    print("Cache Cleared")
    cache.clear()
    return HttpResponse('Cache cleared')