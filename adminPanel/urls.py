from django.urls import path
from . import views


app_name = 'adminPanel'

urlpatterns = [
    path('api/itemlist/', views.ItemDataTableAPI.as_view()),

    path('', views.Dashboard, name='Home'),
    path('citylist/', views.CityList, name='citylist'),

    path('itemlist/', views.ItemList, name='item_list'),
    path('additem/', views.AddItem, name='add_item'),


]
