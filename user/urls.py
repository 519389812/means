from django.urls import path, re_path
from . import views

app_name = "user"

urlpatterns = [
    re_path('^login/$', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('user_setting/', views.user_setting, name="user_setting"),
    path('change_password/', views.change_password, name="change_password"),
    path('check_username_validate/', views.check_username_validate, name="check_username_validate"),
    path('check_password_validate/', views.check_password_validate, name="check_password_validate"),
    path('check_old_password_validate/', views.check_old_password_validate, name="check_old_password_validate"),
    path('check_password_repeat_validate/', views.check_password_repeat_validate, name="check_password_repeat_validate"),
    path('check_lastname_validate/', views.check_lastname_validate, name="check_lastname_validate"),
    path('check_firstname_validate/', views.check_firstname_validate, name="check_firstname_validate"),
    path('check_email_validate/', views.check_email_validate, name="check_email_validate"),
    path('check_question_validate/', views.check_question_validate, name="check_question_validate"),
    path('check_answer_validate/', views.check_answer_validate, name="check_answer_validate"),
    path('check_post_valudate/', views.check_post_valudate, name="check_post_valudate"),
    path(r'set_email_verify/', views.set_email_verify, name="set_email_verify"),
    path(r'send_set_user_verify_email/', views.send_set_user_verify_email, name="send_set_user_verify_email"),
    path(r'pre_reset_password/', views.pre_reset_password, name="pre_reset_password"),
    path(r'pre_reset_password_by_email/', views.pre_reset_password_by_email, name="pre_reset_password_by_email"),
    path(r'send_reset_password_email/', views.send_reset_password_email, name="send_reset_password_email"),
    re_path(r'check_set_user_verify_email/(.*)/$', views.check_set_user_verify_email, name="check_set_user_verify_email"),
    re_path(r'reset_password_by_email/(.*)/$', views.reset_password_by_email, name="reset_password_by_email"),
    path('feedback/', views.feedback, name="feedback"),
    path('get_agreement/', views.get_agreement, name="get_agreement"),
    path('show_agreement/', views.show_agreement, name="show_agreement"),
    path('sign_agreement/', views.sign_agreement, name="sign_agreement"),
]
