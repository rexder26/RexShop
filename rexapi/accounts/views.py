from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Customer,job
from .forms import OrderForm,CreateUserForm,CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='login')
@admin_only
def home(request):
    orderview =  Order.objects.all()
    customerview = Customer.objects.all()

    total_customers = customerview.count()
    total_orders = orderview.count()
    delivered = orderview.filter(status='Delivered').count()
    pending = orderview.filter(status='Pending').count()

    context = {'orders':orderview,'customers':customerview,'delivered':delivered,'pending':pending,'total_orders':total_orders,'total_customers':total_customers}
    return render(request,'account/dashboard.html',context)

@login_required(login_url='login')
def jobs(request):
    jobview = job.objects.all()
    return render(request,'account/jobs.html',{'jobs':jobview})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admins'])
def customer(request,pk):
    customerr = Customer.objects.get(id=pk)
    orderr = customerr.order_set.all()
    orderview =  Order.objects.all()
    total_orders = orderview.count()
    
    myFilter = OrderFilter(request.GET,queryset=orderr)
    orderr = myFilter.qs  
    context = {'customerr':customerr,'orderr':orderr,'total_orders':total_orders,'myfilter':myFilter}
    return render(request,'account/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admins'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('job','status'),extra=5)
    customers = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customers)
    #form = OrderForm(initial={'customer':customers})
    if request.method == "POST":
        formsets = OrderForm(request.POST,instance=customers)
        if formsets.is_valid():
            formsets.save()
            return redirect('home')
    context = {'form':formset}
    return render(request,'account/orderform.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admins'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'account/orderform.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admins'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context = {'form':form,'order':order}
    return render(request,'account/delete.html', context)   

@unauthUser
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            

            user = form.save()
            group = Group.objects.get(name='Customer')
            
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            Customer.objects.create(user=user)
            messages.success(request,'Account Created Successful for '+username)
            return redirect('login')
        else:
            messages.error(request,'Invalid Password!')
            return redirect('registration')
    context = {'forms':form}
    return render(request,'account/register.html',context)

def error_404_handler(request, exception):
    return render(request, 'components/404.html')

@unauthUser
def rexlogin(request):
    if request.method == "POST":
        uname = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request,username=uname,password=passwd)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credential!")
            return redirect('home')
    else:
        return render(request,'account/login.html',{})
    
def rexlogout(request):
    if not request.user.is_authenticated:
        messages.success(request,'Congratulations!')
        return redirect('login')
    logout(request)
    messages.success(request,'Logged Out!')
    return redirect('main')

@login_required(login_url='login')
@allowed_user(allowed_roles=['Customer','admins'])
def userProfile(request):
    order = request.user.customer.order_set.all()

    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {'userorders':order,'delivered':delivered,'pending':pending,'total_orders':total_orders}
    return render(request,'account/profile.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['Customer','admins'])
def profile_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'account/profilesetting.html',context)