from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products, name = 'show_products'),
    path('lab/<int:pk>', views.product_info, name = 'product_info'),
    path('new', views.new_product, name = 'new_product'),
    path('lab/<int:pk>/edit', views.edit_product, name = 'edit_product'),
    path('search/', views.search, name = 'search'),
]
