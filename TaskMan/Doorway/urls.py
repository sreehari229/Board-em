from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('create-acc/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('verify/<slug:token>/', views.email_verification, name='email_verify'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="Doorway/password_reset_complete.html"),
         name="password_reset_complete"),
]
