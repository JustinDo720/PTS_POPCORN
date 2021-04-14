from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeProfilePhoto, ChangeProfileEmail, ChangeUserName, ChangeProfileBio
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
    user_posts = profile.post_set.order_by('-date_of_entry')
    context = {
        'user_profile': profile,
        'user_posts': user_posts,
    }
    return render(request, 'user_profile.html', context)


def edit_user_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    curr_user = User.objects.get(id=profile_id)

    if request.method != 'POST':
        photo_form = ChangeProfilePhoto(instance=profile)
        email_form = ChangeProfileEmail(instance=profile)
        bio_form = ChangeProfileBio(instance=profile)
        username_form = ChangeUserName(instance=curr_user)

    else:
        photo_form = ChangeProfilePhoto(instance=profile, data=request.POST, files=request.FILES)
        email_form = ChangeProfileEmail(instance=profile, data=request.POST)
        bio_form = ChangeProfileBio(instance=profile, data=request.POST)
        username_form = ChangeUserName(instance=curr_user, data=request.POST)
        if photo_form.is_valid()\
                and email_form.is_valid() \
                and bio_form.is_valid\
                and username_form.is_valid():
            photo_form.save()
            email_form.save()
            bio_form.save()
            username_form.save()
            return redirect('users:user_profile', profile_id= profile_id)

    context ={
        'profile': profile,
        'photo_form': photo_form,
        'email_form': email_form,
        'bio_form': bio_form,
        'username_form': username_form
    }
    return render(request, 'edit_user_profile.html', context)
