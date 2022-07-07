from django.http import HttpResponse
from django.shortcuts import redirect, render
from expenses.models import *
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
import json

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

def categoty_summary_data(request):
    # getting total expenses
    total_expenses=list(AddExpence.objects.filter(owner=request.user).values_list('amount', flat=True))
    total_user_expenses=0
    for i in total_expenses:
        total_user_expenses+= i
    # print('total amount of th user.......', total_user_expenses)

    today_date= datetime.date.today()
    # last one month expenses
    one_month_ago= today_date - datetime.timedelta(30*1)
    one_month_summary= AddExpence.objects.filter(owner= request.user, date__gte=one_month_ago, date__lte=today_date).values_list('amount', flat=True)
    all_month_summary= AddExpence.objects.filter(owner= request.user, date__lte=today_date)
    print('.........................................',all_month_summary)
    one_month_total_summary= 0
    for i in one_month_summary:
        one_month_total_summary+=i

    # finding six month data
    final_category={}
    six_months_ago= today_date - datetime.timedelta(30*6)
    summary= AddExpence.objects.filter(owner= request.user, date__gte=six_months_ago, date__lte=today_date)
    def get_category(summary):
        return summary.category
    
    category_list= list(set(map(get_category, summary)))
    print('czat..............',category_list)
    def get_category_amount(category):
        total_amount=0
        filter_by_category= summary.filter(category=category)
        # print('..........filter_by_category.............', filter_by_category)
        for item in filter_by_category:
            total_amount =total_amount+ item.amount
            # print(total_amount)
        return total_amount

    for y in category_list:
        final_category[y] = get_category_amount(y) 


    

    # finding previous month data
    prevous_month_data={}
    prevous_month_query= AddExpence.objects.filter(owner=request.user, date__gte=one_month_ago, date__lte=today_date)
    query= AddExpence.objects.filter(owner=request.user)
    print('all admin data', query)
    print('previous mont data.....',prevous_month_query)

    def get_one_month(prevous_month_query):
        return prevous_month_query.category
    # print(get_one_month(prevous_month_query))
    one_month_cat_list= list(set(map(get_one_month, prevous_month_query)))
    print('.........',one_month_cat_list)
    for i in one_month_cat_list:
        prevous_month_data[i]= get_category_amount(i)
    
    # one_month_data_json= json.dumps(prevous_month_data)
    # print('list data is',one_month_data_json)
    
    # getting others expenses total amount
    total_other_expenses=final_category.get('other')
    final_json=final_category
    final_one_month_summary= prevous_month_data

    # import pdb
    # print(pdb.set_trace())
    expenses={
        'total_user_expenses': total_user_expenses,
        'total_other_expenses': total_other_expenses,
        'final_category': final_category
    }

    return render(request, 'expenses/summary.html', locals() )
    
