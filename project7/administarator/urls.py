from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('a_index/', views.a_index),
    path('admin_login/', views.admin_login),
    path('view_domain/', views.view_domain),
    path('GENERATE_ID/', views.GENERATE_ID),
    path('view_domain_generate/', views.domain_send_mail),
    path('view_donor_generated_id/', views.view_donor_generated_id),
    path('view_donor_purpose/', views.view_donor_purpose),
    path('virtual_loading/', views.virtual_loading),
    path('access_procee_team/', views.access_procee_team),
    path('access_cipher_team/', views.access_cipher_team),
    path('A_logout/', views.A_logout),
    path('admin_payslip_form/', views.admin_payslip_form),
    path('access_domain_team/', views.access_domain_team),
    path('domain_send_mail/<int:id>/', views.domain_send_mail),
    path('process_team_mail/<int:id>/', views.process_team_mail),
    path('cipher_team_mail/<int:id>/', views.cipher_team_mail),
    path('domain_team_mail/<int:id>/', views.domain_team_mail),
    path('create_virtual_box/<int:id>/', views.create_virtual_box),


]