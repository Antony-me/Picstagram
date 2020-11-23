from django.http import request
from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm


def my_profile_view(request):

    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm()
   
    return render(request,'profiles/myprofile.html', {'profile':profile, 'form':form})
