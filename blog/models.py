#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from DjangoUeditor.models import UEditorField

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    """
    分类
    """

    name = models.CharField('名称',max_length=16)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签
    """

    name = models.CharField('名称',max_length=16)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Blog(models.Model):
    """
    博客
    """

    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    #content = models.TextField('正文')
    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    created = models.DateTimeField('发布时间',auto_now_add=True)

    category = models.ForeignKey(Category,verbose_name='分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_get_detail',args=(self.pk,))

@python_2_unicode_compatible
class Comment(models.Model):
    """
    评论
    """

    blog = models.ForeignKey(Blog,verbose_name='博客')

    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=140)

    created = models.DateTimeField('发布时间',auto_now_add=True)

    def __str__(self):
        return self.name