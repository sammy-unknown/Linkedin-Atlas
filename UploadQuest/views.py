from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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
    from time import sleep
    if request.user.is_anonymous:
        print("redirecting to login")
        return redirect('/login')
    update =0
    data_list = []
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        file_name = csv_file.name

        # Convert CSV to list of dictionaries
        csv_data = csv.DictReader(StringIO(csv_file.read().decode('utf-8')))
        data_list = [dict(row) for row in csv_data]

        # Add dictionary field to each record
        record_orgid =1
        for record in data_list:
            record['totalProfiles'] = 0
            record['email'] = 'none'
            record['status']='pending'
            record['id']=str(record_orgid)
            record_orgid +=1


        # Insert data into MongoDB collection
        if db is not None:
            result = collection.insert_many(data_list)

        response_data = {'file_name': file_name}
        return JsonResponse(response_data)

    if db is not None:
        # store_data()
        print("Data should be updated")
        # record['data_dict'] = [{'id': 1, 'first': 'priyam', 'last': 'tomar','email':'none'}, {'id': 2, 'first': 'shubham', 'last': 'saini','email':'none'}]
        # record['status'] = 'done'
        # collection.update_one({'id': record['id']}, {'$set': record})
    return render(request, "templates/upload.html")

def store_data():

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep
    from pyautogui import scroll,click
    opt = Options()
    opt.add_experimental_option("debuggerAddress",f"localhost:8989")
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
    driver.implicitly_wait(5)
    def Wait(xpth):
        return WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpth)))


    def tab(n):
        tn = driver.window_handles[n]
        driver.switch_to.window(tn)

    def seniority():
        try:
            driver.find_element(by=By.CSS_SELECTOR,value=f'#search-filter-panel-st34 > div:nth-child(2) > form > div > div:nth-child(4) > fieldset:nth-child(2) > div > fieldset:nth-child(2) > div > button').click()
        except Exception:
            try:
                driver.find_element(by=By.CSS_SELECTOR,value=f'#search-filter-panel-st34 > div:nth-child(2) > form > div > div:nth-child(4) > fieldset:nth-child(3) > div > fieldset:nth-child(2) > div > button').click()
            except Exception:
                driver.find_element(by=By.CSS_SELECTOR,value=f'#search-filter-panel-st34 > div:nth-child(2) > form > div > div:nth-child(4) > fieldset:nth-child(4) > div > fieldset:nth-child(2) > div > button').click()
        k=1
        sleep(2)
        for i in range(1,10):
            try:
                print(i)
                level = driver.find_element(by=By.XPATH,value=f'/html/body/main/div[1]/div[1]/div[2]/form/div/div[4]/fieldset[3]/div/fieldset[2]/div[3]/div[1]/ul/li[{k}]/div/span[1]').get_attribute('innerText')
                # mnlevl = int(level.split(" ")[1])
                bclevl = level.split(" ")[0]
                if (bclevl=='Entry' or bclevl=='Manager' or bclevl=='Senior' or bclevl=='Owner' or bclevl=='CXO' or bclevl=='VP' or bclevl=='Director'):
                    print(level)
                    driver.find_element(by=By.XPATH,value=f'/html/body/main/div[1]/div[1]/div[2]/form/div/div[4]/fieldset[3]/div/fieldset[2]/div[3]/div[1]/ul/li[{k}]/div/button[1]').click()
                    # driver.page_source
                else:
                    k+=1
                    print(level,'n')
            except IndexError:
                print("ERROE",level)
                break

    new_data = list(collection.find({'status': 'Checking'}))
    if not new_data :
        new_data = list(collection.find({'status': 'pending'}))

    if new_data:
        update = 1
        print("New data found")
        data_list = new_data
        # Update data_list
        for record in data_list:
            company_link = record['company_link']
            data_id = record['id']
            print(data_id)
            # record['status'] = 'done'
            # collection.update_one({'id': record['id']}, {'$set': record})


            tab(0)
            if driver.current_url != company_link:
                driver.get(company_link)
            try:
                driver.find_element(by=By.XPATH,value=f'/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[2]/div/a/span').click()
                sleep(3)
                driver.find_element(by=By.XPATH,value=f'/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li/div/a').click()
            except:
                driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[2]/div/a/span').click()
                sleep(3)
                driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li/div/a').click()
            driver.close()
            tab(0)
            seniority()
            sleep(1)
            i=0
            while i<50:
                try:
                    url=driver.find_element(by=By.XPATH,value=f'/html/body/main/div[1]/div[2]/div[2]/div/ol/li[{i+1}]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/a')
                    title = driver.find_elements(by=By.CSS_SELECTOR,value=f'span[data-anonymize="person-name"]')[i].get_attribute('innerText')
                    desn = driver.find_elements(by=By.CSS_SELECTOR,value=f'span[data-anonymize="title"]')[i].get_attribute('innerText')
                    domain = record['Domain']
                    existing_record = collection.find_one({'id': str(data_id)})

                    profile_url = url.get_attribute('href')
                    profile_url_id = profile_url.split("lead/")[1].split(",")[0]
                    newProfileUrl = f'https://www.linkedin.com/in/{profile_url_id}'
                    if existing_record:
                        existing_data_dict = existing_record.get('data_dict', [])
                        new_data = {'id': i+1, 'first': title.split(" ")[0], 'last': title.split(" ")[1], 'designation':desn,'website':domain,'Profile_Link':newProfileUrl ,'email':'none'}
                        existing_data_dict.append(new_data)
                        collection.update_one({'id': str(data_id)}, {'$set': {'data_dict': existing_data_dict, 'status': 'Checking'}})
                    else:
                        # Otherwise, create a new record with the specified ID
                        data_dict = [{'id': i+1, 'first': title.split(" ")[0], 'last': title.split(" ")[1], 'designation':desn,'website':domain,'Profile_Link':newProfileUrl ,'email':'none'}]
                        record = {'id': str(data_id), 'data_dict': data_dict, 'status': 'Checking'}
                        collection.insert_one(record)

                    print(f"i: {i} and Updating- {title}")
                    driver.execute_script("window.scrollBy(0, 1000);")
                    sleep(1)
                    driver.execute_script("arguments[0].scrollIntoView();", url)

                except Exception as e:
                    print(e)
                    try:
                        print('Page Change')
                        i=0
                        # /html/body/main/div[1]/div[2]/div[2]/div/div[4]/div/button[2]
                        # /html/body/main/div[1]/div[2]/div[2]/div/div[4]/div/button[2]
                        Wait('/html/body/main/div[1]/div[2]/div[2]/div/div[4]/div/button[2]')
                        driver.find_element(by=By.XPATH,value=f'/html/body/main/div[1]/div[2]/div[2]/div/div[4]/div/button[2]').click()

                    except:
                        record = {'id': str(data_id),'status': 'done'}
                        # Find the document with the specified ID and retrieve the data_dict field
                        document = db['my_collection'].find_one({'id': str(data_id)}, {'data_dict': 1})
                        data_dict = document['data_dict']
                        array_length = len(data_dict)
                        collection.update_one({'id': str(data_id)}, {'$set': {'totalProfiles':array_length,'status': 'Checked'}})

                        print('BREAKING')
                        break
                i+=1
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
    return redirect('/')

def account(request):
    return render(request,"templates/account.html")