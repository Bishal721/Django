from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    # return HttpResponse("Hello, This is Bishal's Project")
    return render(request,"crud/index.html")