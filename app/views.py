from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,"index.html")


def Portfolio(request):
    return render(request," Portfolio-Details ")

def Service(request):
    return render(request,"Service-Details ")

def Starter(request):
    return render(request,"starter-page")

def contact_view(request):
    if request.method == 'POST':
        # process form data here
        return HttpResponse("Thanks for contacting us!")
    return render(request, 'contact.html')
