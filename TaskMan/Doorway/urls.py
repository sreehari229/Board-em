from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('create-acc/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('verify/<slug:token>/', views.email_verification, name='email_verify')
]
