
from django.urls import path
from classauth import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('activate/<uidb>/<token>',views.ActivateAccountView.as_view(), name='activate'),
    
]
