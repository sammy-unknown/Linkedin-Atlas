from django.shortcuts import render
# Create your views here.
def Collect(request):
    if request.method == "POST":
        url = request.POST.get("InputBox")
        print(f'URL:{url}')
        from pymongo import MongoClient
        from urllib.parse import quote_plus

        username = "manojtomar326"
        password = "Tomar@@##123"
        cluster_url = "cluster0.ldghyxl.mongodb.net"
        encoded_username = quote_plus(username)
        encoded_password = quote_plus(password)
        connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster_url}/test?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        db = client['mydatabase']  # Replace with your actual database name
        collection=db['Crunchbase']
        collection.insert_one({"url":url,"status":"pending"})
    return render(request,"templates/crunchbase.html")
