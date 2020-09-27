from django.contrib import admin
from django.urls import path, include

import amsite
import users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('amsite/', include('amsite.urls')),
    path('', include('startsite.urls')),
]
