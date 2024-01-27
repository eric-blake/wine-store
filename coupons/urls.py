# from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('apply/<item_id>/', views.coupon_apply, name='coupon_apply'),
    ]



#   url(r'/^apply/$', views.coupon_apply, name='coupon_apply'),