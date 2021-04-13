from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from pts_pops_app.models import Profile, Post
# Create your views here.

def register(request):
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            registered_user = form.save()
            # We are going to use login to instantly login after registering
            login(request, registered_user)
            return redirect('pts_pops_app:index')

    return render(request, 'registration/register.html', {'form':form})


def user_profile(request, profile_id):
    # We are going to use profile to locate our user's info
    profile = Profile.objects.get(id=profile_id)
    user_posts = profile.post_set.all()
    print(profile.user.username)
    context = {
        'user_profile': profile,
        'user_posts': user_posts
    }
    return render(request, 'user_profile.html', context)