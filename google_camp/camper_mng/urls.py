from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^reg$', views.reg, name='reg'),
        url(r'^mod$', views.mod, name='mod'),
        ]