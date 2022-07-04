from django.shortcuts import render, redirect
from userincome.models import AddIncome
from django.contrib import messages

# add income
def income_index(request):
  current_user= request.user
  print(current_user)
  if request.method== 'POST':
    in_amount= request.POST['income_amount']
    des= request.POST['income_des']
    income_source= request.POST['income_source']
    date= request.POST['date']
    try:
      add_income= AddIncome(income_amount=in_amount, date=date, description=des, owner=current_user, source=income_source)
      add_income.save()
      messages.info(request,'Your income is added successfully')
      return redirect('my_income')
    except:
      messages.error(request, 'Something went wrong')
      return render(request, 'income/index.html')

  # getting income data
  income_data= AddIncome.objects.filter(owner=current_user)
  print('income data..................', income_data)

  return render(request, 'income/index.html')

# income edit
def income_edit(request):
  return render(request, 'income/edit_incomes.html')
