from django.urls import path
from . import views


app_name = 'adminPanel'

urlpatterns = [
    path('', views.Dashboard, name='Home'),
    path('citylist/', views.CityList, name='citylist'),
]
