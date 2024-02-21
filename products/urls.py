from . import views
from django.urls import path

urlpatterns = [

    path('products/favourites/', views.favourites, name='favourites'),
    path('add_to_favourites/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),

   


]