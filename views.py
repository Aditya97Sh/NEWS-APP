from django.http import response
from django.shortcuts import render
import requests
API_Key= '7cc022f41cb3450bbd3d9346211a32fd'
# Create your views here.
def home(request):
 url= f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_Key}'
 response= requests.get(url)
 data=response.json()
 articles= data['articles']
 return render(request, 'home.html', {'articles':articles})
