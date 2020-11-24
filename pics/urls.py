from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import post_comment_create_and_list_view

app_name= 'pics'

urlpatterns=[
    path('', post_comment_create_and_list_view, name='main-post-view'),
   
]