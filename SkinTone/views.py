from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'Skintone/index.html')




