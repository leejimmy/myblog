#-*-coding:utf-8-*-
from django.shortcuts import render
from .models import Blog,Comment
from django.http import Http404
from .forms import CommentForm
import re

# Create your views here.
def get_blogs(request):

    #images_url1和images_url2是上传图片的位置
    a1 = Blog.objects.all().order_by('-created')[0]
    con1 = a1.content
    images_url1 = re.findall('src="(.*?)" alt.*',con1)[0]

    a2 = Blog.objects.all().order_by('-created')[1]
    con2 = a2.content
    images_url2 = re.findall('src="(.*?)" alt.*', con2)[0]

    #cont1和cont2是文章过滤掉图片后的文字内容
    cont1 = re.findall('<p>(.*?)</p>',con1)[0]
    cont2 = re.findall('<p>(.*?)</p>',con2)[0]

    ctx = {
        #'blogs':Blog.objects.all().order_by('-created')
        'blog_1':Blog.objects.all().order_by('-created')[0],
        'blog_2':Blog.objects.all().order_by('-created')[1],
        'images_url1':images_url1,
        'images_url2':images_url2,
        'cont1':cont1,
        'cont2':cont2
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