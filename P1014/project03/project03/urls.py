from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('event/', include('event.urls')),
    path('customer/', include('customer.urls')),
    path('community', include('community.urls')),
]
