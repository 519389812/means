from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    email_verify = models.BooleanField(default=False, verbose_name='邮箱验证')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='上次登录IP')

    def get_full_name(self):
        full_name = '%s%s' % (self.last_name, self.first_name)
        return full_name.strip()

    def __str__(self):
        return self.username


class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    version = models.CharField(max_length=30, verbose_name='版本')
    title = models.CharField(max_length=300, verbose_name='协议标题')
    content = RichTextField(max_length=1000000, config_name='default', verbose_name="协议内容")
    must_sign = models.BooleanField(default=True, verbose_name="必须签订")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户协议'
        verbose_name_plural = '用户协议'

    def __str__(self):
        return self.title + " " + self.version


class AgreementSignRecord(models.Model):
    id = models.AutoField(primary_key=True)
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, verbose_name='协议')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户协议签订记录'
        verbose_name_plural = '用户协议签订记录'

    def __str__(self):
        return str(self.id)


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register', '验证'),
        ('reset', '重设'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    email = models.EmailField(verbose_name="邮箱")
    code = models.CharField(max_length=20, verbose_name='验证码')
    type = models.CharField(choices=send_choices, max_length=10, verbose_name='验证码类型')
    close_datetime = models.DateTimeField(verbose_name='过期时间')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = '邮箱验证'

    def __str__(self):
        return self.email


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    content = models.TextField(max_length=800, verbose_name="内容")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = "用户反馈"
        verbose_name_plural = "用户反馈"

    def __str__(self):
        return self.content[:15] if len(self.content) < 15 else self.content[:15] + "..."
