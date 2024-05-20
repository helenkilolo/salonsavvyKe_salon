from django.urls import path
from django.contrib import admin
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),  # Add this for the appointment list view
]
