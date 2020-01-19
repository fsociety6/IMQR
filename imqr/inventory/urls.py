from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

urlpatterns = [

    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.dashboard, name="dashbo"),
    path('item/create/', views.ItemCreateView, name="item_create"),
    path('item/<int:pk>/', views.ItemDetailView, name="item_detail"),
    path('item/service/<int:pk>/', views.CreateServiceView, name="item_service"),
    path('scan/qr/',views.scancode,name='scancode'),
    url('', include('pwa.urls')),
    path('product/',views.productlist),
    path('category/create/', views.CategoryCreateView, name='category_create'),
    path('logout',views.logout),
    path('', views.index,name='index'),
    path('product/', views.productindex,name='productindex'),
    path('product/<int:pk>/', views.productview,name='productshow'),
    path('product/create/', views.productcreate,name='productcreate'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]

