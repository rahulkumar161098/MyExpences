from django.http import HttpResponse
from django.shortcuts import redirect, render
from expenses.models import AddExpence
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

# Create your views here.
def dashboard(request):
    return render (request, 'bash.html')

def base_page(request):
    return render(request, 'home.html')

def addExpence(request):
    current_user= request.user
    expence_data= AddExpence.objects.filter(owner=current_user).order_by('-date')
    # use of value_list()
    # some_data= AddExpence.objects.values_list('id', 'amount', 'category')
    # print(some_data)
    # use of value()
    value_data= AddExpence.objects.values()
    # print(value_data)

    paginator= Paginator(expence_data, 5)
    page_number= request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    print(page_obj)
    context={
        'expence_user_data': expence_data,
        'page_obj': page_obj
    }

    if request.method== 'POST':
        exp_amount= request.POST['add_amount']
        des= request.POST['des']
        exp_category= request.POST['expence_category']
        date= request.POST['date']
        try:
            add_expence= AddExpence(amount=exp_amount, date=date, description=des, owner=current_user, category=exp_category)
            add_expence.save()
            messages.info(request,'Your expence is added successfully')
            return redirect('add_expences')
        except:
            messages .error(request, 'Something went wrong')
            return render(request, 'addExpences.html')

    return render(request, 'addExpences.html', context)

def edit_expense(request, pk):
    if not request.user.is_authenticated:
        return redirect ('user_log')
    edit_expense= AddExpence.objects.get(id=pk)
    if request.method== 'POST':
        amount= request.POST['edit_amount']
        des= request.POST['des']
        exp_category= request.POST['expence_category']
        date= request.POST['date']

        edit_expense.amount=amount
        edit_expense.date= date
        edit_expense.description= des
        edit_expense.category= exp_category
        try:
            edit_expense.save()
            messages.info(request, "Expense update successfully")
            return redirect('add_expences')
        except:
            messages.info(request, "Somethings Went Wrong!")
            return render(request, 'expenses/edit_expense.html')
    # print('........................',edit_expense.owner)
    return render(request, 'expenses/edit_expense.html', locals())

def delete_expense(request, pk):
    if not request.user.is_authenticated:
        return redirect ('user_log')
    delete_expense= AddExpence.objects.get(id=pk)
    delete_expense.delete()
    return redirect('add_expences')
    
