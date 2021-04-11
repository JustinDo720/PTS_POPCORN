from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def community_page(request):
    return render(request, 'community_page.html')