from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login_view, name="login"),
    # url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

    url(r'^register/$', views.register_view, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),

    # create items url
    # url(r'^items/create_item', views.ItemCreateView.as_view(), name="item_create"),
    path('item/create/', views.ItemCreateView, name="item_create"),

    path('item/<int:pk>/', views.ItemDetailView, name="item_detail"),

    # create services url
    path('item/service/<int:pk>/', views.CreateServiceView, name="item_service"),


    path('scan/qr/',views.scancode,name='scancode'),
    path('',views.mainview)

    path('category/create/', views.CategoryCreateView, name='category_create'),
]
