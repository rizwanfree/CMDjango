from django.urls import path
from . import views


app_name = 'adminPanel'

urlpatterns = [
    path('', views.Dashboard, name='Home'),
    path('citylist/', views.CityList, name='citylist'),

    path('itemlist/', views.ItemList, name='item_list'),
    path('add-item/', views.ClientEdit, name='add_item'),
    path('edit-item/<int:id>/', views.ClientEdit, name='edit_item'),


]
