from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.forms import ModelForm
from django.db import models
from operator import itemgetter
import json
import csv

patientList = {}

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    return render(request, '../templates/login.html')


def register(request):
    if request.method == 'POST':  # If the form has been submitted...
        user = 'User: ' + request.POST.get('user_id')
        # return HttpResponse(user)
        return render(request, '../templates/home.html', {'user':user})
    else:
        return HttpResponse("not registered")

    
# Calculates and returns patient severity score based on blood pressure
def getBPScore(age, sex, bp):
    severity = 0

    if sex == "F"
        with open('BP.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[0] == age:
                    if bp.sys > row[1] and bp.sys < row[1] + 5 or bp.dia >= row[2] and bp.dia < row[2] + 5:
                        severity += 1
                    elif bp.sys >= row[1] + 5 and bp.sys < row[1] + 10 or bp.dia >= row[2] + 5 and bp.dia < row[2] + 10:
                        severity += 2
                    elif bp.sys >= row[1] + 10 or bp.dia >= row[2] + 10:
                        severity += 3
     
    elif sex == "M":
        with open('BP.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[0] == age:
                    if bp.sys > row[1] and bp.sys < row[1] + 5 or bp.dia >= row[2] and bp.dia < row[2] + 5:
                        severity += 1
                    elif bp.sys >= row[1] + 5 and bp.sys < row[1] + 10 or bp.dia >= row[2] + 5 and bp.dia < row[2] + 10:
                        severity += 2
                    elif bp.sys >= row[1] + 10 or bp.dia >= row[2] + 10:
                        severity += 3

    else:
        print('Sorry No valid gender found')

    return severity


# Calculates and returns patient severity score based on body temperature
def getTemperatureScore(temp):
    severity = 0

    if temp > 99 and temp <= 101
        severity += 1
    elif temp > 101 and temp <= 104
        severity += 2
    elif temp > 104
        severity += 3
    
    return severity


# Ranks patients based on calculated score of the heart rate
def getHeartRateScore(age, bpm):
    severity = 0

    with open('BPM.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if age >= row[0] and age <= row[1]:
                if bpm > row[2] and bpm < row[1] + 5
                    severity += 1
                elif bpm >= row[2] + 5 and bpm < row[1] + 10
                    severity += 2
                elif bpm > row[2] + 10
                    severity += 3
                
    return severity


# Ranks patients based on calculated score of the vital signs recorded
def rank_patient(request):
    # add new patient data to the list
    data = = json.loads(request.body)

    # Retrieve patient data
    patient_age = int(data.age)
    sex = data.sex
    # bp dict: sys - dia
    blood_pressure = json.loads()
    temperature = int(data.body_temp)
    heart_rate = int(data.heart_rate)

    BPScore = getBPScore(patient_age, sex, blood_pressure)
    temperatureScore = getTemperatureScore(temperature)
    heartRateScore = getHeartRateScore(heart_rate)

    rank = (BPScore + temperatureScore + heartRateScore) / 3
    patientList.update({'priority': 0,'rank': rank, 'wait_time': 0})

    time = 0
    priority = 0
    for patients in sorted(patientList, key = itemgetter('rank'):
        priority += 1
        time += 10
        patients[wait_time] = time
        patients[priority] = priority
    
    return render(request, <add template name>, patientList)
