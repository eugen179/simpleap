from django.shortcuts import render
from .forms import ProductForm
from .models import Product  

def product(request):
    img= 'https://t3.ftcdn.net/jpg/08/68/24/84/360_F_868248419_TjtUJRgcWc43QAeTImHOQJkfoWQqmBdd.jpg'
    return render(request,'index.html',{'image':img})
   