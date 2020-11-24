# from django.conf.urls import url
from .views import my_profile_view, invites_received, profiles_list, invites_list
from django.urls import path


app_name = 'profiles'

urlpatterns = [
    path('profile/', my_profile_view, name='myprofile'),
    path('myinvites/',invites_received, name='myinvites'),
    path('profile-list/',profiles_list, name='profile-list'),
    path('toinvite-list/',invites_list, name='toinvite-list'),
]