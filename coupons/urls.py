# from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('apply_coupon/', views.apply_coupon, name='apply_coupon'),
    ]
