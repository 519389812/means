from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # 通知列表
    path('show_notice/', views.show_notice, name='show_notice'),
    # 更新通知状态
    path('mark_notice_as_read/', views.mark_notice_as_read, name='mark_notice_as_read'),
    path('send_notice/', views.send_notice, name='send_notice'),
    path('jump_to_target/', views.jump_to_target, name='jump_to_target'),
]
