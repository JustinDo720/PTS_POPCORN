from django.shortcuts import render, redirect
from .forms import UserEntries, EditUserEntries, AnonymousEntries
from .models import Post, AnonymousPost
from django.core.paginator import Paginator
from itertools import chain

# Create your views here.
def index(request):
    return render(request, 'index.html')

def community_page(request):
    if request.method != 'POST':
        a_form = AnonymousEntries()
        s_form = UserEntries()
    else:
        a_form = AnonymousEntries(data=request.POST, files=request.FILES)
        s_form = UserEntries(data=request.POST, files=request.FILES)
        if a_form.is_valid() & s_form.is_valid():
            # This is an anonymous user. We let the registered user with some benefits :)
            a_new_comment = a_form.save(commit=True)
            s_new_comment = s_form.save(commit=False)
            s_new_comment.owner = request.user
            s_new_comment.owner_profile = request.user.profile
            a_new_comment.save()
            s_new_comment.save()
            return redirect('pts_pops_app:community_page')

    # Query all posts
    all_posts = Post.objects.order_by('-date_of_entry')
    anonymous_posts = AnonymousPost.objects.order_by('-date_of_entry')
    combined_posts = list(chain(all_posts, anonymous_posts))

    paginator = Paginator(combined_posts, 3)
    print(combined_posts)
    page_number = request.GET.get('page',1 )

    all_posts = paginator.get_page(page_number)



    context = {'all_posts':all_posts, 'a_form': a_form, 's_form': s_form}
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


def remove_post(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('users:user_profile', post_to_delete.owner_profile.user.id)