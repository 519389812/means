from django.db import models
from django.contrib.auth.models import AbstractUser
from team.models import Team


class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, verbose_name="用户组")
    email_verify = models.BooleanField(default=False, verbose_name='邮箱验证')

    def get_full_name(self):
        full_name = '%s%s' % (self.last_name, self.first_name)
        return full_name.strip()

    def __str__(self):
        return self.username


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

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = '邮箱验证'

    def __str__(self):
        return self.email


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    title = models.TextField(max_length=100, verbose_name="标题")
    content = models.TextField(max_length=800, verbose_name="内容")
    ip = models.GenericIPAddressField(verbose_name="IP地址")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")

    class Meta:
        verbose_name = "用户反馈"
        verbose_name_plural = "用户反馈"

    def __str__(self):
        return self.title
