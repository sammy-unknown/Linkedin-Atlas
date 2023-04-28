from django.shortcuts import render
from pymongo import MongoClient
from django.core.paginator import Paginator

# Cache the view for 5 minutes
# @cache_page(60 * 5)
def Analytics(request):
    from urllib.parse import quote_plus
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