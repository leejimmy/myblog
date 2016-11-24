#-*-coding:utf-8-*-
from django.shortcuts import render
from .models import Blog,Comment
from django.http import Http404
from .forms import CommentForm

# Create your views here.
def get_blogs(request):
    ctx = {
        'blogs':Blog.objects.all().order_by('-created')
    }

    return render(request,'index.html',ctx)

def get_detail(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()

    else:
        form = CommentForm(request.POST)
        print "form:",form
        if form.is_valid():
            cleaned_data =  form.cleaned_data
            print "cleaned_data:",cleaned_data
            cleaned_data['blog'] = blog    #添加一个外键，使评论和对应的blog联系起来
            print "cleaned_data['blog']:",cleaned_data['blog']
            print "cleaned_data: ",cleaned_data
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog':blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request,'blog_detail.html',ctx)


def get_photos(request):
    return render(request,'photos.html')