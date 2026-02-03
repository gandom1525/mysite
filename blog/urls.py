from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_page,name='index'),
    path('single',single_page,name='single'),
    path('post-<int:pid>',test,name='test')
    # path('test',test,name='test')



]