from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('api/clients/', views.ClientDataTableAPI.as_view(), name='table-client-list-api'),
    path('clientlist/', views.ClientList, name='client_list'),
    path('clientdetails/<int:id>/', views.ClientDetails, name='client_details'),
    path('edit/<int:id>/', views.ClientEdit, name='client_edit'),
    path('add/', views.ClientEdit, name='client_add')

    
]
