from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm

def post_comment_create_and_list_view(request):
    qs = Post.objects.all()
    profile= Profile.objects.get(user=request.user)

    
    p_form = PostModelForm()
    post_added = False

    profile = Profile.objects.get(user=request.user)
    p_form = PostModelForm(request.POST, request.FILES)

    if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
           
    return render(request,'posts/main.html' , {'qs':qs, 'profile':profile, 'p_form':p_form}) 


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()


    return redirect('pics:main-post-view')