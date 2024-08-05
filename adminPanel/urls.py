from django.urls import path
from . import views
from .views import PortUpdateView, PortListView, PortCreateView

app_name = 'adminPanel'

urlpatterns = [
    path('', views.Dashboard, name='Home'),
    path('citylist/', views.CityList, name='citylist'),

    # Item URLs
    path('itemlist/', views.ItemList, name='item_list'),
    path('add-item/', views.ItemEdit, name='add_item'),
    path('edit-item/<int:id>/', views.ItemEdit, name='edit_item'),

    # Port URLs
    path('port-list/', PortListView.as_view(), name='port-list'),
    path('port-add/', PortCreateView.as_view(), name='port-add'),
    path('port-edit/<int:pk>/', PortUpdateView.as_view(), name='port-edit'),

]
