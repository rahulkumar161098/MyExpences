from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout

# Create your views here.


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

def user_login(request):
    if request.method== 'POST':
        u_name= request.POST['username']
        u_pass= request.POST['password']
        user= authenticate(username=u_name, password= u_pass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html' )


    return render(request, 'authentication/login.html' )

def logged_out(request):
    logout(request)
    return redirect('user_log')




def user_dashboard(request):
    return render(request, 'bash.html')


    
