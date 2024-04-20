from .views import *
from django.urls import path

urlpatterns = [
    path('fake_name/', fake_name, name='fake_name'),
    path('fake_lastname/', fake_lastname, name='fake_lastname'),
    path('fake_number/', fake_number, name='fake_number'),
    path('fake_addres/', fake_addres, name='fake_addres'),
    path('fake_email/', fake_email, name='fake_email'),
    path('fake_pass/', fake_pass, name='fake_pass'),
    path('fake_dob/', fake_dob, name='fake_dob'),
    path('fake_city/', fake_city, name='fake_city'),
    path('fake_banknumber/', fake_banknumber, name='fake_banknumber'),
    path('fake_login/', fake_login, name='fake_login'),
    path('fake_link/', fake_link, name='fake_link'),
    path('fake_autonum/', fake_autonum, name='fake_autonum'),
    path('fake_text/', fake_text, name='fake_text'),
    path('fake_job/', fake_job, name='fake_job'),
]