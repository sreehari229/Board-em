from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_index_page, name='acc-page'),
]