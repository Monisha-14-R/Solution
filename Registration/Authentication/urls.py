from django.urls import path

from Authentication import views


urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('otp-verification/', views.otp_verification_view, name='otp_verification'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('dashboard-view/', views.dashboard_view,name='dashboard'),
    path('send_otp_email/', views.send_otp_email,name='send_otp'),

    ]

