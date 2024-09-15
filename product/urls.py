#product/urls

from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # All products
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_results, name='search_results'),
]
