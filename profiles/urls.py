# from django.conf.urls import url
from .views import my_profile_view
from django.urls import path


app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='myprofile'),
]