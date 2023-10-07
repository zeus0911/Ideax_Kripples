from django.urls import path,include
from .views import *

app_name = 'app'

urlpatterns = [
    path('index', index , name = 'index'),
    path('products', product_view_list, name="product_list"),
    path('product/<pid>/', product_detail_view, name="product-detail"),
    path('category', category_view_list, name="categories"),
    path('category/<cid>/', category_detail_view, name="category-detail"),
    path('dashboard', dashboard, name='dashboard'),
    path('add_product', add_product, name = 'add_product'),
    path('about', about, name='about'),
]