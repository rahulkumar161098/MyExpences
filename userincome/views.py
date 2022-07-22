from email import message
from threading import local
from django.shortcuts import render, redirect
from userincome.models import AddIncome
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

# add income
def income_index(request):
  if not request.user.is_authenticated:
        return redirect ('user_log')
  current_user= request.user
  print(current_user)
  if request.method== 'POST':
    in_amount= request.POST['income_amount']
    des= request.POST['income_des']
    income_source= request.POST['income_source']
    date= request.POST['date']
    try:
      add_income= AddIncome(income_amount=in_amount, date=date, income_desc=des, owner=current_user, income_source=income_source)
      add_income.save()
      messages.info(request,'Your income is added successfully')
      return redirect('my_income')
    except:
      messages.error(request, 'Something went wrong')
      return render(request, 'income/index.html')

  # getting income data
  income_data= AddIncome.objects.filter(owner=current_user)
  # print('income data..................', income_data)
  user_income={
    'income_data': income_data
  }
  # pagination
  paginator= Paginator(income_data, 2)
  page_number= request.GET.get('page')
  page_obj = Paginator.get_page(paginator, page_number)
  print(page_obj)

  return render(request, 'income/index.html', user_income)

# income edit
def income_edit(request, id):
  if not request.user.is_authenticated:
    return redirect ('user_log')
  edit_user_income= AddIncome.objects.get(id=id)
  if request.method=='POST':
    income= request.POST['amount']
    in_desc= request.POST['des']
    in_source= request.POST['income_source']
    in_date= request.POST['date']

    edit_user_income.income_amount= income
    edit_user_income.income_desc= in_desc
    edit_user_income.income_source= in_source
    edit_user_income.date= in_date
    try:
      edit_user_income.save()
      messages.info(request, "Income Update Successfully!")
      return redirect('user_income_index')
    except:
      messages.info(request, "Something went wrong!")
      return render(request, 'income/edit_incomes.html')


  edit_income={
    'edit_user_income': edit_user_income
  }
  return render(request, 'income/edit_incomes.html', edit_income)

def del_income(request, id):
  if not request.user.is_authenticated:
    return redirect ('user_log')
  income_del= AddIncome.objects.get(id=id)
  income_del.delete()
  return redirect ('user_income_index')

def income_summary(request):
  current_user= request.user
  current_date= datetime.date.today()

  # total income
  total_income_query= list(AddIncome.objects.filter(owner=current_user).values_list('income_amount', flat=True))
  # print('total income', total_income_query)
  total_income= 0
  for i in total_income_query:
    total_income+=i

  # one month income
  one_month_ago= current_date - datetime.timedelta(30*1)
  one_month_income= list(AddIncome.objects.filter(owner= current_user, date__gte=one_month_ago, date__lte=current_date).values_list('income_amount', flat=True))
  one_month_total_income= 0
  for i in one_month_income:
    one_month_total_income+=i

  # last six month income of source
  six_month_ago= current_date - datetime.timedelta(30*6)
  six_month_income= list(AddIncome.objects.filter(owner= current_user, date__gte=six_month_ago, date__lte=current_date).values_list('income_amount', flat=True))
  six_month_total_income= 0
  for i in six_month_income:
    six_month_total_income+=i

  # track six month expenses (month wise)
  income_list={}
  incomes= AddIncome.objects.filter(owner=current_user, date__gte=six_month_ago, date__lte=current_date)

  def source(incomes):
    return incomes.income_source

  all_incomes_list= list(set(map(source, incomes)))

  def get_incomes(income_source):
    total=0
    get_income_source= incomes.filter(income_source=income_source)
    for a in get_income_source:
      total= total+a.income_amount
    return total
    
  for y in all_incomes_list:
        income_list[y] = get_incomes(y) 

  # print(all_incomes_list)
  # print(incomes)
  # print(income_list)


  context={
    'total_income': total_income,
    'one_month_total_income': one_month_total_income,
    'six_month_total_income': six_month_total_income
  }

  return render(request, 'income/income_summary.html', locals())
