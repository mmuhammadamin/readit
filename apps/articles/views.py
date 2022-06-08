from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import CommentForm
from .models import Post, Category, Tag


# Create your views here.
def index_view(request):
    blogs = Post.objects.all().order_by('-id')[:9]
    blogs1 = Post.objects.all().order_by('-id')[:2]
    p = Paginator(Post.objects.all().order_by('-id')[:9], 2)
    page = request.GET.get('page')


    blog = p.get_page(page)
    list = []

    for page in range(1, blog.paginator.num_pages+1):
        list.append(page)
    ctx = {
        'blogs': blogs,
        'blogs1': blogs1,
        'blog': blog,
        'list':list
    }

    return render(request, 'index.html', ctx)


def blog_single(request, pk):
    blogs = Post.objects.all().order_by('-id')
    categories = Category.objects.all()
    blog = Post.objects.get(id=pk)
    tags = Tag.objects.all()
    blogs1 = Post.objects.all().order_by('-id')[:3]

    form = CommentForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.post = blog
        obj.save()

        # return redirect('/blog/')

    ctx = {
        'blogs': blogs,
        'categories': categories,
        'blog': blog,
        'tags': tags,
        'blogs1': blogs1,
        'form': form

    }

    return render(request, 'blog-single.html', ctx)


def blog_view(request):
    blogs = Post.objects.all().order_by('-id')[:9]
    blogs1 = Post.objects.all().order_by('-id')[:2]
    p = Paginator(Post.objects.all().order_by('-id')[:9], 3)
    page = request.GET.get('page')

    blog = p.get_page(page)

    search_result = Post.objects.all().order_by('-id')

    result = request.GET.get('search')

    category = request.GET.get('category')

    list=[]

    for page in range(1,blog.paginator.num_pages+1):
        list.append(page)

    tag = request.GET.get('tag')
    if result:
        blogs = search_result.filter(title__icontains=result)

    if category:
        blogs = search_result.filter(category__title__exact=category)

    if tag:
        blogs = search_result.filter(tag__tag__exact=tag)

    ctx = {
        'blogs': blogs,
        'blogs1': blogs1,
        'search_result': search_result,
        'blog': blog,
        'list':list

    }

    return render(request, 'blog.html', ctx)
