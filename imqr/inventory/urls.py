from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$', views.login_view, name="login"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="inventory/registration/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"),
        name="logout"),

    url(r'^register/$', views.register_view, name="register"),

    # create items url
    url(r'^items/create_item', views.ItemCreateView.as_view(), name="item_create"),

    # Item Delete
    url(r'^delete_item/(?P<pk>[0-9]+)/item/$',
        views.ItemDeleteView.as_view(template_name="inventory/item_confirm_delete.html"), name='delete_item'),
]
