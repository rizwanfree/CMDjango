from django.urls import path
from . import views
from .views import PortUpdateView, PortListView, PortCreateView, PortDetailView
from .views import ShippingListView, ShippingCreateView, ShippingUpdateView, ShippingDetailView

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
    path('port-details/<int:pk>/', PortDetailView.as_view(), name='port-details'),
    path('port-delete/<int:pk>/', views.PortDelete, name='port-delete'),

    # Shipping Line URLs
    path('shipping-list/', ShippingListView.as_view(), name='shipping-list'),
    path('shipping-add/', ShippingCreateView.as_view(), name='shipping-add'),
    path('shipping-edit/<int:pk>/', ShippingUpdateView.as_view(), name='shipping-edit'),
    path('shipping-details/<int:pk>/', ShippingDetailView.as_view(), name='shipping-details'),
    path('shipping-delete/<int:pk>/', views.ShippingDelete, name='shipping-delete'),
]
