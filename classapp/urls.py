
from django.urls import path
from classapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('cources/', views.courses),
    path('trainers/',TemplateView.as_view(template_name="trainers.html")),
    path('pricing/',TemplateView.as_view(template_name="pricing.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),
    path('login/',views.login),
    path('signup/',views.signup),
]
