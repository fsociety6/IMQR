from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.login_view, name="login"),
    url(r'^register/$', views.register_view, name="register"),

    # create items url
    url(r'^items/create_item', views.ItemCreateView.as_view(), name="item_create"),
]
