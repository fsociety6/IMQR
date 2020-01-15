from django.conf.urls import url
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login_view, name="login"),
    # url(r'^login/$', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"),name="logout"),

    url(r'^register/$', views.register_view, name="register"),
    path('dashboard/',views.dashboard,name="dashboard"),

    # create items url
    url(r'^items/create_item', views.ItemCreateView.as_view(), name="item_create"),

    # Item Delete
    url(r'^delete_item/(?P<pk>[0-9]+)/item/$',
        views.ItemDeleteView.as_view(template_name="inventory/item_confirm_delete.html"), name='delete_item'),
]
