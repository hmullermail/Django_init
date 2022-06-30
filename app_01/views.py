from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .models import Post, Category

# Create your views here.

def login(request: HttpRequest):
    templateData = {
        'title': 'Login Page',
        }
    
    if request.method == 'GET':
        return render(request, 'app_01/login.html', templateData)
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        django_login(request, user)

        # return HttpResponseRedirect('/home/')
        return redirect('/home/')
        # return render(request, 'app_01/login.html', templateData)
    else:
        templateData['message'] = 'Wrong credentials'
        return render(request, 'app_01/login.html', templateData)

@login_required(login_url='/login')
def home(request):
    templateData = {
        'title': 'Home'
        }
    return render(request, 'app_01/home.html', templateData)

@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return redirect('/login/')






# def home(request):
#     return HttpResponse('Hello World')

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
        'title': 'List of Posts',
        'posts': posts,
        'categories': category
        }
    return render(request, 'app_01/post_list.html', templateData)

def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()
    templateData = {
        'title': post.title,
        'post': post,
        'categories': category
        }
    return render(request, 'app_01/post_show.html', templateData)

