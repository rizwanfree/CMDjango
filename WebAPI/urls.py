from django.urls import path
from . import views

app_name = 'API'

urlpatterns = [
    # Client API URLs
    path('client/table-clients/', views.ClientDataTableAPI.as_view(), name='table-client-list'),

    # Item API URLs
    path('item/table-items/', views.ItemDataTableAPI.as_view(), name='item-table-list'),
]
