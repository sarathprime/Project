from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('process_index/', views.process_index),
    path('process_register_form/', views.process_register_form),
    path('process_login_form/', views.process_login_form),
    path('view_domain_user_detail/', views.view_domain_user_detail),
    path('process_id/', views.process_id),
    path('process_id_1/', views.process_id_1),
    path('process_id_2/', views.process_id_2),
    path('process_id_3/', views.process_id_3),
    path('view_domain_user_purpose/', views.view_domain_user_purpose),
    path('view_domain_user_final/', views.view_domain_user_final),
    path('predection/<int:id>/', views.predection),

    path('domian_send_id_key_file/<int:id>/', views.domian_send_id_key_file),
    path('send_technical_team/<int:id>/', views.send_technical_team),
    path('process_logout/', views.process_logout),
    path('view_domains_request/', views.view_domains_request),
    path('view_dmoin_Request/', views.view_dmoin_Request),


]