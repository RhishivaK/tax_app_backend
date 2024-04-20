from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('auth/', include('_auth.urls')),
    path('income-tax/', include('tax.urls')),
    path('vehicle-tax/', include('tax.urls')),
    path('business-tax/', include('tax.urls')),
    path('asset-tax/', include('tax.urls'))
]
