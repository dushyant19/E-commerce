from django.shortcuts import render
from .models import *
# Create your views here.

def Cart(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        orderitems = OrderItem.objects.filter(customer=Customer)
        order = orderitems[0].order
    else :
        orderitems = []
        order = {'get_cart_total':0,'get_number_of_items':0}
    context={'items':orderitems,'order':order}
    return render(request,'store/cart.html',context)

def Checkout(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        orderitems = OrderItem.objects.filter(customer=Customer)
        order = orderitems[0].order
    else :
        orderitems = []
        order = {'get_cart_total':0,'get_number_of_items':0}
    context={'items':orderitems,'order':order}
    return render(request,'store/Checkout.html',context)

def Store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)