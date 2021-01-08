# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")


def result(request):
    
    lm = joblib.load('final_model.csv')
    
    lis = []
    
    lis.append(request.GET['Avg. Area Income'])
    lis.append(request.GET['Avg. Area House Age'])
    lis.append(request.GET['Avg. Area Number of Rooms'])
    lis.append(request.GET['Avg. Area Number of Bedrooms'])
    lis.append(request.GET['Area Population'])
    
   
    
    ans = lm.predict([lis])
    
    return render(request,'result.html',{'ans':ans})


    