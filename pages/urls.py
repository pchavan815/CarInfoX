from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('emi', views.emi, name='emi'),
    path('car_emi_calculator', views.car_emi_calculator, name='car_emi_calculator'),
    path('accessories', views.accessories, name='accessories'),

]
