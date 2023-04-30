from django.shortcuts import render
from pymongo import MongoClient
from django.core.paginator import Paginator
from urllib.parse import quote_plus
from django.http import JsonResponse

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
db = client['mydatabase']
    # Retrieve data from the collection
data = list(db.my_collection.find())

def Analytics(request):
    if request.method == "POST":
        # print(request.POST)
        # get the data from the form
            # Retrieve the data from your MongoDB collection
        items = data
        # # print(request.POST)
        orginitem = items[0]['id']
        for i in range(int(orginitem),int(orginitem)+10):
            if i < len(items):
                item = items[i]
                item_id = item['id']
                latest_email = request.POST.get(f"updatedEmail{item_id}")
                if latest_email:
                    db.my_collection.update_one({'id': item_id}, {'$set': {'email': latest_email}})
                    print(f"Query Update to {latest_email}")

    # Create a Paginator object with 10 items per page
    paginator = Paginator(data, 10)

    # Get the current page number from the query string parameter 'page'
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)

    # If there is no data, show a message in the template
    message = ""
    if not page_obj:
        message = "No data found."

    context = {  
        'items': page_obj,
        'message': message
    }

    return render(request, "analytics.html", context)



def refresh_data(request):
    # Retrieve data from the collection
    data = list(db.my_collection.find())
    return JsonResponse({'message': 'Data refreshed successfully.'})