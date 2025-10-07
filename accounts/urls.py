# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('password_reset/', views.password_reset_view, name='password_reset'),
path('set_new_password/', views.set_new_password_view, name='set_new_password'),

path('confirmation/', views.confirmation_view, name='confirmation_view'),

path('logout/', views.logout, name='logout'),

path('logout/', views.logout_user, name='logout_user'),  # the real logout

]
