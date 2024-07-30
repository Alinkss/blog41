from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    data = "13.06.2024"
    current_data = datetime.datetime.now()
    
    day_name = current_data.strftime('%A')
    full_date = current_data.strftime('%d.%m.%Y')
    return HttpResponse(f"""
         <h1> Data: {data} </h1>               
         <h2> Another data: {full_date} </h2>
         <h3> Day: {day_name}  </h3>                
    """)
# Create your views here.
