from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    number = 400
    title = "Main page"
    context = {"title": title}
    return render(request, "helloweb/index.html", context)



    # return HttpResponse(f"""
    #         <h1> Hello from Django! </h1>
    #         <h2> number is {number} </h2>
    #         <a href="index"> Index </a>                   
    # """)

def django(request):
    return None
