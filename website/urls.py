from django.urls import path
from website.views import *
# http_test,json_test

app_name='website'

urlpatterns = [
    path('',home_page,name='index'),
    path('about',about_page,name='about'),
    path('contact',contact_page,name='contact')


    # path('http_test',http_test),
    # path('json_test',json_test)
]