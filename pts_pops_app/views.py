from django.shortcuts import render, redirect
from .forms import UserEntries, EditUserEntries, AnonymousEntries, FeedbackForm, QuestionMaker, AddChoice
from .models import Post, Question, Choice
from django.core.paginator import Paginator
from itertools import chain
from django.http import Http404, HttpResponseRedirect
import os
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def community_page(request):
    if request.method != 'POST':
        if request.user.is_authenticated:
            form = UserEntries()
        else:
            form = AnonymousEntries()
    else:
        if request.user.is_authenticated:
            form = UserEntries(data=request.POST, files=request.FILES)
            if form.is_valid():
                s_new_comment = form.save(commit=False)
                s_new_comment.owner = request.user
                s_new_comment.owner_profile = request.user.profile
                s_new_comment.save()
                return redirect('pts_pops_app:community_page')
        else:
            form = AnonymousEntries(data=request.POST, files=request.FILES)
            if form.is_valid():
                a_new_comment = form.save(commit=True)
                a_new_comment.owner = None
                a_new_comment.owner_profile = None
                a_new_comment.save()
                return redirect('pts_pops_app:community_page')

        # Query all posts
    all_posts = Post.objects.order_by('-date_of_entry')

    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page', 1)

    all_posts = paginator.get_page(page_number)

    AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')
    context = {'all_posts': all_posts, 'form':form, 'AWS_BUCKET_BASEURL': AWS_BUCKET_BASEURL}
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

    if post_requested.owner != request.user:
        raise Http404

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

    if post_to_delete.owner != request.user:
        raise Http404

    post_to_delete.delete()
    return redirect('users:user_profile', post_to_delete.owner_profile.user.id)


def submit_feedback(request):
    if request.method != 'POST':
        form = FeedbackForm()
    else:
        form = FeedbackForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pts_pops_app:index')

    context = {
        'form': form
    }

    return render(request, 'submit_feedback.html', context=context)


def custom_404(request, exception):
    return render(request, 'error_handle/404.html')


def custom_500(request):
    return render(request, 'error_handle/500.html')


def view_full_post(request, post_id):
    post_to_view = Post.objects.get(id=post_id)
    AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')
    context = {
        'post_to_view': post_to_view,
        'AWS_BUCKET_BASEURL': AWS_BUCKET_BASEURL
    }
    return render(request, 'view_full_post.html', context)


def admin_add_question(request):
    if not request.user.is_superuser:
        raise Http404
    if request.method != 'POST':
        form = QuestionMaker()
    else:
        form = QuestionMaker(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pts_pops_app:admin_add_choice')
    context ={'form': form}
    return render(request, 'poll/admin_add_question.html', context)


def admin_add_choice(request):
    if not request.user.is_superuser:
        raise Http404

    if request.method != 'POST':
        form = AddChoice()
        print('I am not supposed t0 be here')
    else:
        form = AddChoice(data= request.POST, files= request.FILES)
        if form.is_valid():
            new_choice = form.save(commit=False)
            question_id = new_choice.question.id
            new_choice.save()
            return redirect('pts_pops_app:admin_view_choice', question_id)
    context ={'form': form}
    return render(request, 'poll/admin_add_choice.html', context)


def admin_view_choice(request, question_id):
    question_requested = Question.objects.get(id=question_id)
    all_choices = question_requested.choice_set.order_by('-choice_post_date')
    AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')

    context= {
        'question_requested' : question_requested,
        'all_choices' : all_choices,
        'AWS_BUCKET_BASEURL': AWS_BUCKET_BASEURL,
    }
    return render(request, 'poll/admin_view_choice.html', context)


# Show all the different voting polls.
def vote_homepage(request):
    all_questions = Question.objects.all()
    return render(request, 'poll/vote_homepage.html', {'all_questions': all_questions})


# Show the exact question and choices
def show_question(request, question_id):
    question_requested = Question.objects.get(id=question_id)
    all_choices = question_requested.choice_set.all()
    AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')

    context = {
        'question_requested': question_requested,
        'all_choices': all_choices,
        'AWS_BUCKET_BASEURL': AWS_BUCKET_BASEURL,
    }
    return render(request, 'poll/show_question.html', context)


# Where we up the count if the choice was selected by the user
def voteMechanism(request, question_id):
    question_requested = Question.objects.get(id=question_id)

    try:
        # This means we will try to find a choice with that id from the input field
        selected_choice = question_requested.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Show the voting form again
        return render(request, 'poll/vote_homepage.html')
    else:
        # THe choice exist now we need to boost the coutner by 1
        selected_choice.votes += 1
        selected_choice.save()
        # We are using HttpResponse to add that extra args that is usually needed and the redirect function doesn't provide
        return HttpResponseRedirect(reverse('pts_pops_app:results', args=(question_requested.id,)))


# Show all the results of the choices selected
def results(request, question_id):
    question_requested = Question.objects.get(id=question_id)
    all_choices = question_requested.choice_set.all()
    AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')

    context = {
        'question_requested': question_requested,
        'all_choices': all_choices,
        'AWS_BUCKET_BASEURL': AWS_BUCKET_BASEURL
    }

    return render(request, 'poll/results.html', context)

