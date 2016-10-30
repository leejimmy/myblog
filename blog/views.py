from django.shortcuts import render
from .models import Blog

# Create your views here.
def get_blogs(request):
    ctx = {
        'blogs':Blog.objects.all().order_by('-created')
    }

    return render(request,'blog_list.html',ctx)