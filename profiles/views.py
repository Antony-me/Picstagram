from django.http import request
from django.shortcuts import render
from .models import Profile


def my_profile_view(request):

    profile = Profile.objects.get(user=request.user)
   
    return render(request,'profiles/myprofile.html', {'profile':profile})
