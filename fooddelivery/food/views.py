from django.http import HttpResponse
from django.shortcuts import render
from food.models import Services,Checkout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')
    
def about(request):
    return render(request,'about.html')   

def contact(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        reason=request.POST.get('reason')
        contact=Services(email=email,name=name,phone=phone,reason=reason)
        contact.save()
  
    return render(request,'contact.html')    

def checkout(request):
    if request.method=='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        quantity=request.POST.get('quantity')
        creditcardno=request.POST.get('creditcardno')
        exp=request.POST.get('exp')
        ccv=request.POST.get('ccv')
        checkout=Checkout(email=email,name=name,phone=phone,address=address,quantity=quantity,creditcardno=creditcardno,exp=exp,ccv=ccv)
        checkout.save()
    return render(request,'checkout.html') 