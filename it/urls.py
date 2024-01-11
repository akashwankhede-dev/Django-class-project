
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('classapp.urls')),
    path('classauth/',include('classauth.urls'))
]
