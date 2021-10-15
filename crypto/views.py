import requests
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'crypto/index.html')


def get_bittrex(request, pair):
    response = requests.get(f'https://api.bittrex.com/v3/markets/{pair}/ticker')
    if response.status_code == 200:
        return JsonResponse(response.json())
    return {'lastTradeRate': '0'}