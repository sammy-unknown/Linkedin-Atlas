from django.shortcuts import render,redirect
from pymongo import MongoClient
from django.core.paginator import Paginator
from urllib.parse import quote_plus

from pymongo import UpdateOne
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
# Query all documents in the collection

def Analytics(request):
    db = client['mydatabase']
    collection = db['my_collection']
    data = list(db.my_collection.find().sort('_id', 1))
    paginator = Paginator(data, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    linktotal_pages = paginator.num_pages
    total_documents = collection.count_documents({})
    totalCheckedProfiles = collection.count_documents({'status': 'Checked'})
    # Use the $sum operator to calculate the total count of the 'totalProfiles' field
    result = collection.aggregate([
        {
            '$group': {
                '_id': None,
                'total_count': {'$sum': '$totalProfiles'}
            }
        }
    ])

    # Extract the total count from the result
    total_profiles_count = result.next()['total_count']
    currentChecking = collection.find_one({"status":"Checking"})
    message = ""
    if not page_obj:
        message = "No data found."

    context = {
        'items': page_obj,
        'message': message,
        'total_documents': total_documents,
        'totalpages': linktotal_pages,
        'Company':str(currentChecking['Company']),
        'Domain':str(currentChecking['Domain']),
        'id':int(currentChecking['id']),
        'totalProfiles':currentChecking['totalProfiles'],
        'totalCheckedProfiles':totalCheckedProfiles,
        'total_profiles_count':total_profiles_count,
    }
    return render(request, "templates/analytics.html", context)


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
        pageUpdate = []
        for data in company['data_dict']:
            datai = int(data['id'])
            if not knk:
                i = int(request.POST.getlist('item_id')[datai])-1
                knk = i+10
            latest_email = request.POST.get(f"updatedEmail{int(i)}")
            if latest_email != 'None' and latest_email:
                pageUpdate.append(UpdateOne({'id': pk, 'data_dict.id': i}, {'$set': {'data_dict.$.email': latest_email}}))
                print(f"[{i}]: Query Update {latest_email}")
                
            if i>knk:
                break
            i+=1
        db.my_collection.bulk_write(pageUpdate)
        # print(company['data_dict'])
        if str(request.POST.get('checkcheckboxes')) == 'selectAll':
            i-=1
            # print("All Checbox are selected")
            updates = []
            for p in range(i, 400):
                try:
                    for new_data_dict in company['data_dict']:
                        if new_data_dict['id'] == p:
                            first = new_data_dict['first']
                            last = new_data_dict['last']
                            domain = new_data_dict['website'].replace("https","").replace("http","").replace("/","").replace("www.","")
                            patrnn = request.POST.getlist(f"patternTransfer")[0]
                            latest_email = f'{patrnn.replace("lastname", last).replace("firstname", first).replace("firstname", first).replace("firstinitial", first[0]).replace("lastinitial", last[0]).lower()}@{domain}'
                            if latest_email:
                                updates.append(UpdateOne({'id': pk, 'data_dict.id': p}, {'$set': {'data_dict.$.email': latest_email}}))
                                print(f"[{p}]: Query Update {latest_email}")
                except IndexError:
                    break


            db.my_collection.bulk_write(updates)
            
    db = client['mydatabase']
    newData = company.get('data_dict', [])

    paginator = Paginator(newData, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    message = ""
    if not page_obj:
        message = "No data found."

    title = company['Company']
    status = company['status']
    profiles = company['totalProfiles']
    total_pages = paginator.num_pages
    context = {
        'companies': page_obj,
        'message': message,
        'mainTitle':title,
        'profiles':profiles,
        'totalpages':total_pages,
        'status':status,
        'verification':status,
    }

    return render(request, "templates/viewdata.html", context)
