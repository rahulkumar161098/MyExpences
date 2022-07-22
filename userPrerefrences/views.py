from django.http import HttpResponse
from django.shortcuts import render
import os
import json
from django.conf import settings
from userPrerefrences.models import UserPreferences

# Create your views here.



def preferences(request):
    user_exist= UserPreferences.objects.filter(user=request.user).exists()
    # user_preference= None
    print('user exist................',user_exist)
    
    if user_exist:
        user_preference= UserPreferences.objects.get(user=request.user)
        print('............................', user_preference)
    # import pdb
    # pdb.set_trace()
    if request.method=='GET':
        currency_data=[]

        file_path= os.path.join(settings.BASE_DIR, 'currencies.json')
        with open(file_path, 'r') as json_file:
            json_data= json.load(json_file)
            for k,v in json_data.items():
                currency_data.append({'key':k, 'value':v})

        # print(currency_data)   
        # for debugg
        # import pdb
        # pdb.set_trace()

        return render(request, 'currency.html', {'currencies':currency_data})
    else:
        currency= request.POST['currency']
        if user_exist:
            user_preference.currency=currency
            user_preference.save()
            return HttpResponse('saved')
        else:
            UserPreferences.objects.create(user=request.user, currency=currency)
            return render(request, 'currency.html')
