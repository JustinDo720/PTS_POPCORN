from django.shortcuts import render, redirect
from .forms import UserEntries, EditUserEntries
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')

def community_page(request):
    # Query all posts
    all_posts = Post.objects.all()

    context = {'all_posts':all_posts}
    return render(request, 'community_page.html', context=context)

def community_post(request):
    # We are going to use UserEntries form to allow our users to post on the community page
    if request.method != 'POST':
        form = UserEntries
    else:
        # We are going to use files so request.FILES is where we get all of the files
        form = UserEntries(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            # Cannot assign "3": Post.Owner must be a User instance we can't use request.user.id
            new_comment.owner = request.user # request.user is a User Instance
            new_comment.owner_profile = request.user.profile
            new_comment.save()
            return redirect('pts_pops_app:community_page')

    context = {'form':form}
    return render(request, 'community_post.html', context=context)


def edit_post(request, post_id):
    post_requested = Post.objects.get(id=post_id)
    if request.method != 'POST':
        form = EditUserEntries(instance=post_requested)
    else:
        form = EditUserEntries(instance=post_requested, data= request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
            # We will redirect them to user profile page. Maybe make a message that saids its been updated in community
            return redirect('users:user_profile', profile_id= post_requested.owner.id)
    context = {
        'post_requested': post_requested,
        'form': form
    }

    return render(request, 'edit_post.html', context)
