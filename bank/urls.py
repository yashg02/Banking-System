from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('users/',views.users,name="Users"),
    path('profile/<int:acc>',views.profile,name="Profile"),
    path('search/',views.search,name="Search"),
    path('transfer/',views.transfer,name="Transfer"),
    path('handletransfer/',views.handletransfer,name="HandleTransfer")
]