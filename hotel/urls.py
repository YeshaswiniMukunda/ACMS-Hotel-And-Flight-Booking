from django.urls import path
from . import views

urlpatterns = [

    path('', views.hotel_search, name='hotel_search'),
]