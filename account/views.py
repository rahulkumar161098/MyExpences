from locale import currency
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from expenses.models import AddExpence
from userPrerefrences.models import UserPreferences
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from itertools import chain
# from django.contrib.messages import constants as messages
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

# register user
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        fname= request.POST['fname']
        lname= request.POST['lname']
        uname= request.POST['email']
        password= request.POST['password']
        
        try:
            save_user= User.objects.create_user(first_name=fname, last_name=lname, username=uname, password= password)

            save_user.save()
            return redirect('user_log')
        except:
            return render(request, 'authentication/register.html')

# login user
def user_login(request):
    if request.method== 'POST':
        u_name= request.POST['username']
        u_pass= request.POST['password']
        user= authenticate(username=u_name, password= u_pass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Imvalid Email Id/Password')
            return render(request, 'authentication/login.html' )
    return render(request, 'authentication/login.html' )

# logout user
def logged_out(request):
    logout(request)
    return redirect('user_log')

def user_dashboard(request):
    if request.user.is_authenticated:
        current_user= request.user
        expence_data= AddExpence.objects.filter(owner=current_user).order_by('-date')
        datalen=len(expence_data)
        print(expence_data)
        paginator= Paginator(expence_data, 8)
        page_number= request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        # print(page_obj)
        context={
        'expence_user_data' : expence_data,
        'page_obj' : page_obj,
        'datalen' : datalen
        }
        return render(request, 'addExpences.html', context)
    else:
        return redirect('/login')

# edit user details
def user_details(request):
    if not request.user.is_authenticated:
        return redirect('user_log')
    
    user= User.objects.all().get(username= request.user)
    selected_currency= UserPreferences.objects.get(user= request.user)

    merge_query= User.objects.filter(username=request.user).values_list('username').union(UserPreferences.objects.filter(user=request.user).values_list('currency'))
    print('merged query...........',merge_query)

    context={
        'user': user,
        'selected_currency': selected_currency,
        'merge_query': merge_query
    }
    print(request.user)
    return render(request, 'profile/user_details.html', context)

def edit_user_details(request, id):
    currency= UserPreferences.objects.get(id=id)
    context={
        'currency': currency
    }
    print(currency)
    return render(request, 'profile/user_detail_edit.html', locals())

def user_service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index_page(request):
    return render(request, 'index.html')

    
