from django.urls import path
from . import views

urlpatterns = [
    path('forget-password/', views.forget_password_page, name='forget_password_page'),
    path('verify-otp/', views.verify_otp_page, name='verify_otp_page'), 
    path('reset-password/', views.reset_password_page, name='reset_password_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
