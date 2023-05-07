from django.shortcuts import render,redirect
from pymongo import MongoClient
from django.core.paginator import Paginator
from urllib.parse import quote_plus
from django.http import JsonResponse
from django.http import Http404
from bson import ObjectId

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


def Analytics(request):
    db = client['mydatabase']
    data = list(db.my_collection.find())
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    message = ""
    if not page_obj:
        message = "No data found."

    context = {
        'items': page_obj,
        'message': message
    }

    return render(request, "analytics.html", context)


def company_website(request, pk):
    if request.user.is_anonymous:
        print("redirecting to login")
        return redirect('/login')
    db = client['mydatabase']
    collection = db['my_collection']
    company = collection.find_one({'id': pk})
    knk =0
    # Here i am updaing email with corresponding pattern
    if request.method =="POST":
        print("form submit")
        for data in company['data_dict']:
            datai = int(data['id'])
            if not knk:
                i = int(request.POST.getlist('item_id')[datai])-1
                knk = i+10
            latest_email = request.POST.get(f"updatedEmail{int(i)}")
            if latest_email:
                db.my_collection.update_one({'id': pk, 'data_dict.id': i}, {'$set': {'data_dict.$.email': latest_email}})
                print(f"Query Update to {i} {latest_email}")
            # if i>knk:
            #     break
            i+=1

            # print("New loop is going to start")
        
            # for p in range(i,100):
            #     try:
            #         new_data_dict = company['data_dict'][p]
            #         first = new_data_dict['first']
            #         last = new_data_dict['last']
            #         domain = new_data_dict['website']
            #         latest_email = 
            #         if latest_email:
            #             db.my_collection.update_one({'id': pk, 'data_dict.id': p}, {'$set': {'data_dict.$.email': latest_email}})
            #             print(f"Query Update to {i} {latest_email}")
            #     except IndexError:
            #         break
    db = client['mydatabase']
    newData = company.get('data_dict', [])

    paginator = Paginator(newData, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    message = ""
    if not page_obj:
        message = "No data found."

    context = {
        'companies': page_obj,
        'message': message
    }

    return render(request, "templates/viewdata.html", context)
