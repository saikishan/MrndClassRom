from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('users/', views.UserView.as_view() ,name='account-create')
]