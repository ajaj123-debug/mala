from django.contrib import admin
from django.urls import path
from app import views
from app.views import *
from app.views import monthwise_report
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sardar/', admin.site.urls),
    path('login', views.user_login, name='loginn'),
    path('home/', views.home, name='home'),
    path('accounts/login/', manager_login, name='manager_login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('add_deduction/', views.add_deduction, name='add_deduction'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    # path('generate_report/', views.generate_report, name='generate_report'),
    path('generate_user_report/', views.generate_user_report, name='generate_user_report'),
    path('monthwise-report/', monthwise_report, name='monthwise_report'),
    path('namaz-times/', views.namaz_times_view, name='namaz_times'),
    path('', views.index, name='index'),
]