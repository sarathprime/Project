from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('final_domain_index/', views.final_domain_index),
    path('domian_register_form/', views.domian_register_form),
    path('domian_login_form/', views.domian_login_form),
    path('domain_logout/', views.domain_logout),
    path('domain_payment/', views.domain_payment),
    path('domain_access_1/', views.domain_access_1),
    path('domain_access_2/', views.domain_access_2),
    path('domain_accept_1/', views.domain_accept_1),
    path('view_user_details/', views.view_user_details),
    path('domain_request_id/', views.domain_request_id),
    path('final_final_decrypt/', views.final_final_decrypt),
    path('dec11/<int:id>/', views.dec11),
    path('final_decrypt/', views.final_decrypt),
    path('domain_decrypt_enter/', views.domain_decrypt_enter),
    path('view_file/', views.view_file),
    path('domain_file_enter/', views.domain_file_enter),
    path('domain_request_id_2/', views.domain_request_id_2),


]