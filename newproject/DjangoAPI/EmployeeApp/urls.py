from django.urls import re_path as url
from EmployeeApp import views

urlpatterns=[
    url(r'^departement$',views.departementApi),
    url(r'^departement/([0-9]+)$',views.departementApi)
]