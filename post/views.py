from django.shortcuts import render, redirect
from math import ceil

# Create your views here.
from post.models import Post


def post_list(request):
    page = int(request.GET.get("page", 1))      # 当前页码
    total = Post.objects.count()                # 新闻总数
    per_page = 10                               # 每页显示新闻数量
    pages = ceil(total / per_page)              # 总共多少页

    start = (page - 1) * per_page               # 每页的开始条数
    end = start + per_page                      # 每页的结束条数
    posts = Post.objects.all().order_by('-id')[start:end]           # 获取所有按照时间排序显示
    data = {
        'posts': posts,
        'pages': range(pages),
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