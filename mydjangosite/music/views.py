from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
#create your views here
from .models import *
from .forms import orderForm
def home(request):
    Orders = order.objects.all()
    Customers = Customer.objects.all()
    total_customers = Customers.count()
    total_orders = Orders.count()
    delivered = Orders.filter(status='Delivered').count()
    pending = Orders.filter(status='Pending').count()

    context ={'Customers':Customers , 'Orders':Orders ,'total_customers':total_customers ,'total_orders': total_orders,'delivered': delivered ,'pending':pending }      #The key in the dictionary needs to be passed in the html template for loop

    return render(request , 'music/dashboard.html' , context)

def products(request):
    products = product.objects.all()
    return render(request , "music/products.html" , {'products':products})



def getcustomer(request, pk):
    cust = Customer.objects.get(id=pk)    #accesses the database
    orders = cust.order_set.all()   #quering customers child object from models field,in set id always use lowercase
    order_count = orders.count()
    context =  {'cust':cust ,'orders':orders ,'order_count':order_count}
    return render(request , "music/Customer.html" ,context)

def createorder(request,pk):
    getord = Customer.objects.get(id=pk)

    form = orderForm()
    if request.method == 'POST':
       # print("printing post:",request.POST)
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form }
    return render(request , "music/order_form.html" ,context)

def updateorder(request, pkey):     #the user data is prefiled in this so we can update it
    getorder = order.objects.get(id=pkey)
    form = orderForm(instance=getorder)
    if request.method == 'POST':
        form = orderForm(request.POST,instance=getorder)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "music/order_form.html", context)

def deleteorder(request, pk):
    item = order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, "music/delete.html", context)

