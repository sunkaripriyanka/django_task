from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cart', views.Users)

urlpatterns = [
    path('',include(router.urls)),	
    url(r'^login/', views.login,name ='login'),
    url(r'^signup/', views.signup,name='signup'),
    url(r'^filter_product/', views.order_product,name='order_product'),
    url(r'^order/', views.filter_product,name='filter_product'),
]