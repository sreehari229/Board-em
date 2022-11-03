from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('create-acc/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('verify/<slug:token>/', views.email_verification, name='email_verify'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('password-reset/<token>/' , views.password_reset , name="password-reset"),
]

handler404 = "Doorway.views.page_not_found_view"