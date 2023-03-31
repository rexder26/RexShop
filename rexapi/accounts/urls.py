from django.urls import path,include
from .views import home,jobs,customer,createOrder,updateOrder,deleteOrder,registerPage,rexlogin,rexlogout,userProfile, profile_settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('jobs/', jobs,name='job'),
    path('customers/<int:pk>', customer,name='customer'),
    path('createorder/<int:pk>',createOrder,name="create_order"),
    path('updateorder/<int:pk>',updateOrder,name="update_order"),
    path('deleteorder/<int:pk>',deleteOrder,name="delete_order"),
    path('register/',registerPage,name='registration'),
    path('login/',rexlogin, name='login'),
    path('',rexlogin),
    path('logout/',rexlogout, name='logout'),
    path('profile/',userProfile, name='profilepage'),
    path('settings/',profile_settings,name='settings'),
    path('reset/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_send/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_complete /',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
