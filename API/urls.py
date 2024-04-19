from .views import *
from django.urls import path

urlpatterns = [
    path('fake_name/<str:lang>/<str:gender>/', fake_name, name='fake_name'),
    path('fake_lastname/<str:lang>/<str:gender>/', fake_lastname, name='fake_lastname'),
    path('fake_number/<str:lang>/', fake_number, name='fake_number'),
    path('fake_addres/<str:lang>/<str:full>/', fake_addres, name='fake_addres'),
    path('fake_email/<str:lang>/', fake_email, name='fake_email'),
    path('fake_pass/<str:lang>/', fake_pass, name='fake_pass'),
    path('fake_dob/<str:lang>/', fake_dob, name='fake_dob'),
    path('fake_city/<str:lang>/', fake_city, name='fake_city'),
    path('fake_banknumber/<str:lang>/', fake_banknumber, name='fake_banknumber'),
    path('fake_login/<str:lang>/', fake_login, name='fake_login'),
    path('fake_link/<str:lang>/', fake_link, name='fake_link'),
    path('fake_autonum/<str:lang>/', fake_autonum, name='fake_autonum'),
    path('fake_text/<str:lang>/', fake_text, name='fake_text'),
    path('fake_job/<str:lang>/', fake_job, name='fake_job'),
]