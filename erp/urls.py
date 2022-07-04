from django.urls import path
from .views import (CategoryDeleteView, CategoryFormView,
                    CategoryListView, CategoryCreateView, CategoryUpdateView,
                    DashboardView,
                    ProductCreateView, ProductDeleteView,
                    ProductListView, ProductUpdateView
                    )

app_name = 'erp'

urlpatterns = [
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

    # Panel
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
