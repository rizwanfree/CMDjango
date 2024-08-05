from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('clientlist/', views.ClientList, name='client-list'),
    path('clientdetails/<int:id>/', views.ClientDetails, name='client-details'),
    path('edit/<int:id>/', views.ClientEdit, name='client-edit'),
    path('add/', views.ClientEdit, name='client_add'),
    path('clients/delete/<int:pk>/', views.DeleteClient, name='delete-client'),

    
]
