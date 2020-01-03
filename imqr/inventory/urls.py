from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('product/', views.productindex,name='productindex'),
    path('product/<int:pk>/', views.productview,name='productshow'),
    path('product/create/', views.productcreate,name='productcreate'),
]