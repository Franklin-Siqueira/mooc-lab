from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {"home_page": "active"}
    return render(request, "home.html", context)

def contact(request):
    context = {"contact_page": "active"}
    return render(request, "contact.html", context)