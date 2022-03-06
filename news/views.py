from django.shortcuts import render
from. models import Category

# Create your views here.

def index(request):
    data= {
        'categoryData': Category.objects.all()
    }
    return render(request,'pages/home/home.html',data)

def about(request):
    return render(request,'pages/about/about.html')

