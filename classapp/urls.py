
from django.urls import path
from classapp import views

urlpatterns = [
    path('',views.index,name='index'),
    
]
