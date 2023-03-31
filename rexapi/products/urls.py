from django.urls import path,include
from .views import productlist, productdetail, locationlist, locationdetail
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import admin_only

urlpatterns = [
    path('product/', login_required(admin_only(productlist.as_view()),login_url='login'),name='main'),
    path('product/<int:pk>/', login_required(admin_only(productdetail.as_view()),login_url='login')),
    path('location/', login_required(admin_only(locationlist.as_view()),login_url='login')),
    path('location/<int:pk>', login_required(admin_only(locationdetail.as_view()),login_url='login')),
]
