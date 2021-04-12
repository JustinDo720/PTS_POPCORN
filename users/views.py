from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
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