from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('user_index/', views.user_index),
    path('user_register/', views.user_register),
    path('submit/', views.submit),
    path('user_login/', views.user_login),
    path('domain_register_form/', views.domain_register_form),
    path('domain_purpose_form/', views.domain_purpose_form),
    path('user_virtual/', views.user_virtual),
    path('domin_user_p/', views.domin_user_p),
    path('user_logout/', views.user_logout),



]