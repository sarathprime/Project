from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('cipher_index/', views.cipher_index),
    path('cipher_register_form/', views.cipher_register_form),
    path('cipher_login/', views.cipher_login),
    path('view_user_datas_from_domain/', views.view_user_datas_from_domain),
    path('cipher_id/', views.cipher_id),
    path('view_encrypted/', views.view_encrypted),
    path('view_decrypted/', views.view_decrypted),
    path('cipher_id_1/', views.cipher_id_1),
    path('cipher_id_2/', views.cipher_id_2),
    path('send_id/', views.send_id),
    path('cipher_logout/', views.cipher_logout),
    path('generate_random/', views.generate_random),
    path('enc/<int:id>/', views.enc),
    path('enc1/<int:id>/', views.enc1),
    path('dec/<int:id>/', views.dec),
    path('domin_send_id_key/<int:id>/', views.domin_send_id_key),
    path('send_enc_domin/<int:id>/', views.send_enc_domin),


]