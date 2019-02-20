from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Posts
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Posts.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'posts/create.html', {'form': form}) 