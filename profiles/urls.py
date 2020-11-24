# from django.conf.urls import url
from .views import my_profile_view, invites_received, profiles_list
from django.urls import path


app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='myprofile'),
    path('myinvites/',invites_received, name='myinvites'),
    path('profile-list/',profiles_list, name='profile-list'),
]