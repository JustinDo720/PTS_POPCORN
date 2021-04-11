from django.shortcuts import render, redirect
from .forms import UserEntries
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
            new_comment.save()
            return redirect('pts_pops_app:community_page')

    context = {'form':form}
    return render(request, 'community_post.html', context=context)