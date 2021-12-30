from django.shortcuts import render
from requests.auth import HTTPBasicAuth

import requests
API_url='https://api.stagingeb.com'
API_KEY='l7u502p8v46ba3ppgvj5y2aad50lb9'
#json='?page=1&limit=20&happened_after=2020-03-01T23%3A26%3A53.402Z&happened_before=2025-03-01T23%3A26%3A53.402Z'

# Create your views here.

def home(request):
    #url= f'https://api.stagingeb.com/v1/contact_requests?page=1&limit=20&happened_after=2020-03-01T23%3A26%3A53.402Z&happened_before=2025-03-01T23%3A26%3A53.402Z'
    #url= f'{API_url}contact_requests{json}'
    #method = "get"
    url= f'{API_url}'
    auth = HTTPBasicAuth('apikey','{API_KEY}')
    response= requests.get(url,headers=None,auth=auth)
    data= response.json()
    print(data)

    #content= data['content']
    context= {

        'data':data
    }

    return render(request, 'easybroker_api/home.html', context)