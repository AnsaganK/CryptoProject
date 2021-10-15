from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bittrex/<str:pair>', views.get_bittrex, name='get_bittrex')
]