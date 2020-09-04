from django.contrib import admin
from django.urls import path, include

import amsite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amsite/', include('amsite.urls')),
    path('', include('startsite.urls')),
]
