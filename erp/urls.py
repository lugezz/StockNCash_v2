from django.urls import path
from .views import (CategoryDeleteView, CategoryFormView,
                    CategoryListView, CategoryCreateView, CategoryUpdateView,
                    ClientCreateView, ClientDeleteView,
                    ClientListView, ClientUpdateView,
                    DashboardView,
                    ProductCreateView, ProductDeleteView,
                    ProductListView, ProductUpdateView,
                    SaleCreateView, SaleDeleteView,
                    SaleListView, SaleUpdateView
                    )

app_name = 'erp'

urlpatterns = [
    # Panel
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Categorias
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),

    # Productos
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Clientes
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # Ventas
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
]
