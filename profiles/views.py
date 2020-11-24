from django.db import models
from django.http import request
from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def my_profile_view(request):

    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    return render(request,'profiles/myprofile.html', {'profile':profile, 'form':form, 'confirm':confirm})


def invites_received(request):
    profile = Profile.objects.get(user=request.user)
    invites = Relationship.objects.invatations_received(profile)


    return render(request,'profiles/my_invite.html', {'invites':invites})



def invites_list(request):
    user = request.user
    toinvites = Profile.objects.get_all_profiles_to_invite(user)

    return render(request,'profiles/toinvite_list.html', {'toinvites':toinvites})


def profiles_list(request):
    user = request.user
    profiles = Profile.objects.get_all_profiles(user)

    person= User.objects.get(username__iexact=request.user) 
    person_profile = Profile.objects.get(user=person)

    print(person_profile)

    return render(request,'profiles/profiles_list.html', {'profiles':profiles, 'persons':person_profile})


def profilesListView(ListView):
    model = Profile
    pass
