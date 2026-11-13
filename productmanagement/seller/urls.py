from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='seller/login.html'
    ), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product/add/', views.product_create, name='product_create'),

    path('product/edit/<int:pk>/', views.product_update,
         name='product_update'),

    path('product/delete/<int:pk>/', views.product_delete,
         name='product_delete'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]