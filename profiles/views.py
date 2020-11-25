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

@login_required(login_url='/accounts/login/')
def invites_received(request):
    profile = Profile.objects.get(user=request.user)
    invites = Relationship.objects.invatations_received(profile)


    return render(request,'profiles/my_invite.html', {'invites':invites})


@login_required(login_url='/accounts/login/')
def invites_list(request):
    user = request.user
    toinvites = Profile.objects.get_all_profiles_to_invite(user)

    return render(request,'profiles/toinvite_list.html', {'toinvites':toinvites})

@login_required(login_url='/accounts/login/')
def profiles_list(request):
    user = request.user
    profiles = Profile.objects.get_all_profiles(user)

    person= User.objects.get(username__iexact=request.user) 
    person_profile = Profile.objects.get(user=person)

    print(person_profile)

    return render(request,'profiles/profiles_list.html', {'profiles':profiles, 'persons':person_profile})


@login_required(login_url='/accounts/login/')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
     
        return render(request, 'results.html', {'results': results})
        
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})



def profilesListView(ListView):
    model = Profile
    pass


