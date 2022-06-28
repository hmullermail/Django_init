from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def home_param(request, post_id):
    return HttpResponse('Hello World: %s' % post_id)

def post_list(request):
    if 'category_id' in request.GET:
        # category = Category.objects.get(id=request.GET['category_id'])
        posts = Post.objects.filter(categories=request.GET['category_id'])   
    else:
        posts = Post.objects.all()
    category = Category.objects.all()
    templateData = {
        'posts': posts,
        'categories': category
        }
    return render(request, 'post_list.html', templateData)

def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()
    templateData = {
        'post': post,
        'categories': category
        }
    return render(request, 'post_show.html', templateData)

