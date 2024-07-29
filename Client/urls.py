from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('api/clients/', views.ClientDataTableAPI.as_view(), name='table-client-list-api'),
    path('clientlist/', views.ClientList, name='client_list'),
    
]
