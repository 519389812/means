from django.db import models
from user.models import User
from ckeditor.fields import RichTextField


class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='类别名称')

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"

    def __str__(self):
        return self.name


class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=30, verbose_name="标识码")
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, verbose_name="类别")
    title = models.CharField(max_length=200, verbose_name='名称')
    content = RichTextField(max_length=1000000, config_name='default', verbose_name="内容")
    hidden_content = RichTextField(max_length=10000, null=True, blank=True, config_name='default', verbose_name='隐藏内容')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "收录内容"
        verbose_name_plural = "收录内容"

    def __str__(self):
        return self.title


class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="收录内容")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    score = models.IntegerField(verbose_name="评分")
    content = models.TextField(max_length=800, verbose_name="评分理由")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "评分"
        verbose_name_plural = "评分"

    def __str__(self):
        return self.content


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, verbose_name="评分对象")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    content = models.TextField(max_length=200, verbose_name="内容")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="评分时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return self.content


class Recommendation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField(max_length=100, verbose_name="推荐内容")
    url = models.URLField(max_length=100, verbose_name="地址")
    content = models.TextField(max_length=800, verbose_name="推荐理由")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "推荐"
        verbose_name_plural = "推荐"

    def __str__(self):
        return self.title
