from django.shortcuts import render , render_to_response
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Contact

from django.http import HttpResponse
# Create your views here.

"""def index(request):
    return render_to_response('index.html')"""

# global variable being declared here
global_csv_file_string = ""

def index(request):
    data1= {'firstdata': 'First Data', 'secondata': 'Second Data'}
    data2= "Data: 2"


    context= {
        'Data1': data1,
        'Data2': data2,
        }
    return render(request, 'index.html', context)


def stats(request):

    return render_to_response('stats.html')


def visualisation(request):
    global global_csv_file_string

    a = global_csv_file_string
#code for making the csv file in a string with [,]  separating the rows
    s = ""
    s2 = ""
    for i in a:
        if i == "\n":
            s = s +",]"
            s2 = s2 + ",],"
        elif i == "\r":
            pass
        else:
            s = s+i
            s2 = s2+i

    s = s +  ",]"
    s2 = s2+ ",]"
    temp1 = []
    temp2 = []
    temps = ""

    # converting string csv to rows in a list
    for i in s:
        if i == ",":
            temp1.append(temps)
            temps = ""
        elif i == "]":
            temp2.append(temp1)
            temp1 = []
        else:
            temps = temps + i


    print("type : ")
    print(type(s))

    sendata = []
    for i in temp2:
        for b in i:
            sendata.append(b)
            break

    context = {'Data' : sendata,'temp2':s2}
    return render(request, 'visual.html', context)



# for uploading csv...

"""
Try not changing the code in contact_upload, if there are any changes required, have a backup.
sending the value of the data_set variable to the web page
"""

def contact_upload(request):
    # global var being used
    global global_csv_file_string
    template = "stats.html"
    prompt = {
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")
    data_set = csv_file.read().decode('utf-8')

    # global var = data_set (type: <str>)
    global_csv_file_string = data_set

    context = {'Data' :"Done Uploading"}

    return render(request, template, context)


# line 57 new function being added
def getwords(request):

    # global var
    global global_csv_file_string

    # post request
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

    template = "visual.html"



    result = "False"
    a = global_csv_file_string
#code for making the csv file in a string with [,]  separating the rows
    s = ""
    s2 = ""
    for i in a:
        if i == "\n":
            s = s +",]"
            s2 = s2+",],"
        elif i == "\r":
            pass
        else:
            s = s+i
            s2 = s2+i

    s = s +  ",]"
    s2 = s2 + ",]"

    temp1 = []
    temp2 = []
    temps = ""

    # converting string csv to rows in a list
    for i in s:
        if i == ",":
            temp1.append(temps)
            temps = ""
        elif i == "]":
            temp2.append(temp1)
            temp1 = []
        else:
            temps = temps + i


    finali = []
    search = name

    tempostring = ""
    iter = 0
    while(iter<(len(name))):

        if name[iter]=="%" and name[iter+1]=="2" and name[iter+2]=="0":
            iter = iter + 3
            tempostring = tempostring + " "
        else:
            tempostring = tempostring + name[iter]
            iter= iter+1

    search = tempostring
    # search for all instances of it
    for i,val in enumerate(temp2):
        for j in val:
            if j == search:
                finali.append(i)


    # finarr is the final result
    finarr = []
    for i in finali:
        finarr.append(temp2[i][:])


    sendata = []
    for i in temp2:
        for b in i:
            sendata.append(b)
            break

    context = {'datasent':finarr,'Data':sendata,'temp2':s2}

    return render(request, template, context)
