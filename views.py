from django.shortcuts import render , render_to_response , redirect
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Contact
from django.template import Context, loader
from django.http import HttpResponse
import cv2
import sqlite3
import re
from django.views.decorators.csrf import csrf_exempt
import os
import requests

from PIL import Image

import pytesseract

from django.http import HttpResponse
from django import db
db.connections.close_all()


picurl = ""
# Create your views here.

"""def index(request):
    return render_to_response('index.html')"""


# running scanner code :

def runscanner(request):
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    #Add Paras' CV2 code here
    conn = sqlite3.connect('db_store')
    cur = conn.cursor()
    cur.execute( " Create table if not exists RCData(state text, registration_no text primary key,serialno text,name text,swd_of text,address text, vehicle_class text, model text, makers_name text , year_of_manufacture text, chassis_no text,engine_no text,reg_date text, valid_date text, road_tax_upto text, seating_capacity text, no_of_cylinders text, horse_power text, fuel_used text, color text,purpose_code text, wheel_base text,cc text, weight text,body_type text,standing_capacity text) ")
    #cur.execute(" Create table if not exists Data(state text, registration_no text primary key,swd_of text,address text, class_of_vehicle text, model text, makers_name text , year_of_manufacture text, chassis_no text, valid_upto text, road_tax_upto text, dealers_data text, seating_capacity integer, hpa_lease_with text, no_of_cylinders integer, horse_power integer, fuel_used text, color text, date_of_issue text ) ")
    conn.commit()
    t = " "+str(request)
    temp=[]
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    kar = pytesseract.image_to_string(Image.open('/Users/anirudhrv/Desktop/Misc/BMSHackathan/RCReader/myapp/rc.jpeg'), lang='eng').upper()

    # REGEX
    REGNO = re.compile(r'[A-Z]{2}([0-9]{2}|O[0-9])[A-Z]{2}[0-9]{4}')
    CHASSIS = re.compile(r'[0-9A-Z]{17}')
    ENGINE = re.compile(r'[0-9A-Z]{8}[0-9A-Z]{1,10}')
    FUEL = re.compile(r'PETR(O|0)L')
    MAKERS = ['MARUTHI','TOYOTA','HYUNDAI','CHEVORLET','TATA','SKODA']
    NAME = re.compile(r'[A-Z]+[A-Z]\s[A-Z]+[A-Z](\n|\s[A-Z]+[A-Z]*\n)')
    DATE = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
    MANUDATE = re.compile(r'[0-9]{2}(/|-)[0-9]{4}')

    STATES = {'TN':'Tamil Nadu',
          'AN':'Andaman and Nicobar',
          'AP':'ANDHRA PRADESH',
          'KA': 'Karnataka',
          'HR': 'Haryana',
          'TS': 'Telangana',
          'BR': 'Bihar',
          'MP': 'Madhya Pradesh',
          }

    # regno
    regno = REGNO.search(kar).group()

    # state
    state = regno[:2]
    state = STATES[state]

    # owner
    name = NAME.search(kar).group()

    # chassis and engine
    chassis = CHASSIS.search(kar).group()

    def hasDigit(s):
        return any(char.isdigit() for char in s)

    engines = ENGINE.findall(kar)
    for engine in engines:
        if hasDigit(engine) and engine != regno and engine != chassis:
            break

    # dates (reg and valid)
    dates = DATE.findall(kar)
    import datetime
    now = datetime.datetime.now()
    for date in dates:
        year = int(date[6:])
        if year > now.year:
            expiry_date = date
        else:
            start_date = date
            tax_date = date[:6] + str(int(date[6:])+15)


    #fuel type
    if FUEL.search(kar) == None:
        fuel = 'DIESEL'
    else:
        fuel = 'PETROL'

    # manufacture date
    manudate = MANUDATE.search(kar).group()

    # maker
    for m in re.findall(r'[A-Z][A-Z]+',kar):
        if m in MAKERS:
            maker = m
            break


    row_entry={'state': state,
           'registration_no': regno,
           'serialno': 'null',
           'swd_of':'null',
           'address': 'null',
           'vehicle_class' : 'null',
           'model': 'null',
           'makers_name': maker,
           'year_of_manufacture': manudate,
           'chassis_no': chassis,
           'engine_no':engine,
           'reg_date': start_date,
           'valid_date': expiry_date,
           'road_tax_upto': tax_date,
           'seating_capacity':'null',
           'no_of_cylinders':'null',
           'horse_power':'null',
           'fuel_used': fuel,
           'color':'null',
           'purpose_code':'null',
           'wheel_base': 'null',
           'cc': 'null',
           'weight': 'null',
           'body_type': 'null',
           'standing_capacity': 'null',
           }

    print(row_entry)

    l = []
    for k,v in row_entry.items():
        l.append(v)

    list_to_be_entered=list()
    for key in row_entry:
        list_to_be_entered.append(row_entry[key])

    list_to_be_entered.append("Null")
    t1=tuple(list_to_be_entered)

    print(t1)
    print(len(t1))
    cur.execute("Insert into RCData values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",t1)
    conn.commit()
    print("Insertion successful")
    return HttpResponse('')


# adding register for login:
def register(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"


    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    print(request)
    return HttpResponse(username)
# adding ajax function here :

# global variable being declared here
global_csv_file_string = ""

def index(request):
    data1= {'firstdata': 'First Data', 'secondata': 'Second Data'}
    data2= "Data: 2"

    context= {
        'Data1': data1,
        'Data2': data2,
        }
    return render(request, 'test.html', context)


def stats(request):
    return render_to_response('stats.html')



def first(request):
        context= {'data':'InsertHere'}
        return render(request, 'index.html', context)


# new stuff
def getajaxwords(request):
    data = request.POST['data']

    extendthis = ["State|",
    "Registration_No|",
    "Owner|",
    "Model|",
    "Makers_Name|",
    "Year_of_Manufacture|",
    "Chassis_No|",
    "Engine_No|",
    "Reg_Date|",
    "Valid_Date|",
    "Road_Tax_Upto|",
    "Fuel_Used|"]
    temp = []
    conn = sqlite3.connect('db_final')
    cur = conn.cursor()
    cur.execute( " Create table if not exists RCData(state text, registration_no text primary key,serialno text,name text,swd_of text,address text, vehicle_class text, model text, makers_name text , year_of_manufacture text, chassis_no text,engine_no text,reg_date text, valid_date text, road_tax_upto text, seating_capacity text, no_of_cylinders text, horse_power text, fuel_used text, color text,purpose_code text, wheel_base text,cc text, weight text,body_type text,standing_capacity text) ")
    #cur.execute(" Create table if not exists Data(state text, registration_no text primary key,swd_of text,address text, class_of_vehicle text, model text, makers_name text , year_of_manufacture text, chassis_no text, valid_upto text, road_tax_upto text, dealers_data text, seating_capacity integer, hpa_lease_with text, no_of_cylinders integer, horse_power integer, fuel_used text, color text, date_of_issue text ) ")
    conn.commit()
    t = " "+str(request)
    # extraction of post :
    finstr = ""
    count = 0
    for i in t:
        if i == "=":
            count = 1
        elif count == 1:
            finstr = finstr + i
        elif i == "'>":
            count = 0
        else:
            pass


    finstr = finstr[:len(finstr)-2]
    # finstr is the extracted word
    # part2 : search the word
    name = finstr
    str1="%"+name+"%"
    try:
        #conn = sqlite3.connect(db_file)
        s=cur.execute("SELECT * FROM RCData")
        req="SELECT * FROM RCData WHERE registration_no='"+data+"'"
        s=cur.execute(req)
        i=-1
        j=-1
        #temp=[]
        for rows in s.fetchall():
            i += 1
            t2=[]
            temp.append(t2)
            for words in rows:
                j += 1
                temp[i].append(words+"|")
                #print(words,end="\n")
            j = 0

    except Error as e:
        print(e)
        pass

    #template = "index.html"

    cur.close()
    conn.close()

    #context = {'datasent':temp}
    #print(len(temp))


    temp2 = []
    for i in temp:
        for j in i:
            temp2.append(j)


    fintemp = []
    for i in extendthis:
        fintemp.append(i)

    for i in temp2:
        fintemp.append(i)
    print(fintemp)
    return HttpResponse(fintemp)

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

@csrf_exempt
def mobilescan(request):


    maker = " "
    manudate= " "
    chassis= " "
    state= " "
    engine= " "
    start_date= " "
    expiry_date= " "
    tax_date= " "
    fuel= " "
    print("working")
    url = 'http://10.60.2.42:8080/'
    cam = cv2.VideoCapture(url)
    arr = []
    flag = 0
    framecount = 0
    exit = 0
    while True:
        framecount+=1
        ret, frame = cam.read()
        if framecount < 50:
            continue
        if framecount % 5 != 0:
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('image', frame)
        #imS = cv2.resize(frame, (960, 540))
        #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
        _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
        contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for contour in contours:

            # get rectangle bounding contour
            [x,y,w,h] = cv2.boundingRect(contour)

            # discard areas that are too large
            #if h>300 and w>300:
                #continue

            # discard areas that are too small
            if h<300 or w<350:
                continue

            # draw rectangle around contour on original image
            fake = frame.copy()
            cv2.rectangle(fake,(x,y),(x+w,y+h),(255,0,255),2)
            #cv2.imshow('image', fake)
            flag += 1
            roi = gray[y:y+h, x:x+w]
            arr.append(roi)
            name = 'blur' + str(flag) +'.jpg'
            print(flag)
            cv2.imwrite(name, arr[flag-1])
            #outname = 'out' + str(i) + '.jpg'
            #out = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
            #cv2.imwrite(outname, out)

            if flag == 10:
                variances = []
                for i in range(10):
                    variances.append(variance_of_laplacian(arr[i]))
                m = max(variances)
                index = [i for i, j in enumerate(variances) if j == m][0]
                path = '/Users/anirudhrv/Desktop/Misc/BMSHackathan/RCReader/sih1/static/img'
                outfile = 'output.jpg'
                cv2.imwrite(os.path.join(path ,outfile), arr[index])
                mobile = cv2.resize(arr[index], (720,480))
                cv2.imwrite(os.path.join(path ,"mobile.jpg"),mobile)
                exit = 1
                break

        if exit:
            break

    print('Done')
    r = requests.get("https://api.thingspeak.com/update?api_key=EPO4PIK2ZNDJC9LL&field1=1")

    print("WORKING BOSS")
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    #Add Paras' CV2 code here
    conn = sqlite3.connect('db_store')
    cur = conn.cursor()
    cur.execute( " Create table if not exists RCData(state text, registration_no text primary key,serialno text,name text,swd_of text,address text, vehicle_class text, model text, makers_name text , year_of_manufacture text, chassis_no text,engine_no text,reg_date text, valid_date text, road_tax_upto text, seating_capacity text, no_of_cylinders text, horse_power text, fuel_used text, color text,purpose_code text, wheel_base text,cc text, weight text,body_type text,standing_capacity text) ")
    #cur.execute(" Create table if not exists Data(state text, registration_no text primary key,swd_of text,address text, class_of_vehicle text, model text, makers_name text , year_of_manufacture text, chassis_no text, valid_upto text, road_tax_upto text, dealers_data text, seating_capacity integer, hpa_lease_with text, no_of_cylinders integer, horse_power integer, fuel_used text, color text, date_of_issue text ) ")
    conn.commit()
    t = " "+str(request)
    temp=[]
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    kar = pytesseract.image_to_string(Image.open('/Users/anirudhrv/Desktop/Misc/BMSHackathan/RCReader/sih1/static/img/output.jpg'), lang='eng').upper()
    print(kar)
    # REGEX
    REGNO = re.compile(r'[A-Z]{2}([0-9]{2}|O[0-9])[A-Z]{2}[0-9]{4}')
    CHASSIS = re.compile(r'[0-9A-Z]{17}')
    ENGINE = re.compile(r'[0-9A-Z]{8}[0-9A-Z]{1,10}')
    FUEL = re.compile(r'PETR(O|0)L')
    MAKERS = ['MARUTHI','TOYOTA','HYUNDAI','CHEVORLET','TATA','SKODA']
    NAME = re.compile(r'[A-Z]+[A-Z]\s[A-Z]+[A-Z](\n|\s[A-Z]+[A-Z]*\n)')
    DATE = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
    MANUDATE = re.compile(r'[0-9]{2}(/|-)[0-9]{4}')

    STATES = {'TN':'Tamil Nadu',
          'AN':'Andaman and Nicobar',
          'AP':'ANDHRA PRADESH',
          'KA': 'Karnataka',
          'HR': 'Haryana',
          'TS': 'Telangana',
          'BR': 'Bihar',
          'MP': 'Madhya Pradesh',
          }

    # regno
    regno = REGNO.search(kar).group()

    # state
    state = regno[:2]
    state = STATES[state]

    # owner
    name = NAME.search(kar).group()

    # chassis and engine
    chassis = CHASSIS.search(kar).group()

    def hasDigit(s):
        return any(char.isdigit() for char in s)

    engines = ENGINE.findall(kar)
    for engine in engines:
        if hasDigit(engine) and engine != regno and engine != chassis:
            break

    # dates (reg and valid)
    dates = DATE.findall(kar)
    import datetime
    now = datetime.datetime.now()
    for date in dates:
        year = int(date[6:])
        if year > now.year:
            expiry_date = date
        else:
            start_date = date
            tax_date = date[:6] + str(int(date[6:])+15)


    #fuel type
    if FUEL.search(kar) == None:
        fuel = 'DIESEL'
    else:
        fuel = 'PETROL'

    # manufacture date
    manudate = MANUDATE.search(kar).group()


    # maker
    for m in re.findall(r'[A-Z][A-Z]+',kar):
        if m in MAKERS:
            maker = m
            break

    row_entry={'state': state,
           'registration_no': "118",
           'serialno': 'null',
           'swd_of':'null',
           'address': 'null',
           'vehicle_class' : 'null',
           'model': 'null',
           'makers_name': maker,
           'year_of_manufacture': manudate,
           'chassis_no': chassis,
           'engine_no':engine,
           'reg_date': start_date,
           'valid_date': expiry_date,
           'road_tax_upto': tax_date,
           'seating_capacity':'null',
           'no_of_cylinders':'null',
           'horse_power':'null',
           'fuel_used': fuel,
           'color':'null',
           'purpose_code':'null',
           'wheel_base': 'null',
           'cc': 'null',
           'weight': 'null',
           'body_type': 'null',
           'standing_capacity': 'null',
           }

    print(row_entry)

    l = []
    for k,v in row_entry.items():
        l.append(v)

    list_to_be_entered=list()
    for key in row_entry:
        list_to_be_entered.append(row_entry[key])

    list_to_be_entered.append("Null")
    t1=tuple(list_to_be_entered)

    print(t1)
    print(len(t1))
    cur.execute("Insert into RCData values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",t1)
    conn.commit()
    print("Insertion successful")

    return HttpResponse('')

def picturesend(request):


    context = {'data':'oo'}
    return render(request, 'showpic.html', context)
