from django.shortcuts import render, redirect

# Create your views here.
from post.models import Post


def post_list(request):
    data = {

    }
    return render(request,'post_list.html',context=data)


def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    data = {

    }
    return render(request, 'create_post.html', context=data)


def edit_post(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
    data = {
        'post': post
    }
    return render(request, 'edit_post.html', context=data)


def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    data = {
        'post': post
    }
    return render(request, 'read_post.html', context=data)


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    data = {
        'posts': posts
    }
    return render(request, 'search.html', context=data)