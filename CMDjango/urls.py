from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

urlpatterns = [
    path('api/', include('WebAPI.urls')),
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminPanel.urls')),
    path('client/', include('Client.urls')),
]
