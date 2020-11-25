# from django.conf.urls import url
from .views import my_profile_view, invites_received, profiles_list, invites_list
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/', my_profile_view, name='myprofile'),
    path('myinvites/',invites_received, name='myinvites'),
    path('profilelist/',profiles_list, name='profile-list'),
    path('toinvitelist/',invites_list, name='toinvite-list'),
    path('search/', views.search_profile, name='search'),
]