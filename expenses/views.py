from ast import Add
from django.shortcuts import redirect, render
from expenses.models import AddExpence
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render (request, 'bash.html')

def base_page(request):
    return render(request, 'home.html')

def addExpence(request):
    current_user= request.user
    if request.method== 'POST':
        amount= request.POST['amount']
        des= request.POST['des']
        exp_category= request.POST['expence_category']
        date= request.POST['date']
        try:
            add_expence= AddExpence(amount=amount, date=date, description=des, owner=current_user, category=exp_category)
            add_expence.save()
            messages.info(request,'Your expence is added successfully')
            return redirect('add_expences')
        except:
            return render(request, 'addExpences.html')

    return render(request, 'addExpences.html')
