from django.db import models
from user.models import User
from ckeditor.fields import RichTextField


def default_post_type():
    return Type.objects.get_or_create(name="普通")[0].id


class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='板块名称')

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = "板块"

    def __str__(self):
        return self.name


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='类别名称')

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    classification = models.ForeignKey(Classification, null=True, blank=True, on_delete=models.CASCADE, verbose_name="板块")
    type = models.ForeignKey(Type, default=default_post_type(), on_delete=models.CASCADE, verbose_name="类别")
    title = models.TextField(max_length=200, null=True, blank=True, verbose_name='标题')
    content = RichTextField(max_length=10000000, verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发送人')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    parent_post = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='回复对象')
    related_post = models.JSONField(null=True, blank=True, max_length=300, verbose_name='回复关系')

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return str(self.id)
