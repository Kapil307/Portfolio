from django.urls import path
from .import views



urlpatterns = [
    path('',views.index),
    path('portfolio/',views.Portfolio),
    path('service/',views.Service),
    path('starter/',views.Starter),
    path('contact/', views.contact_view, name='contact')
]
