"""means URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import means.views as main_views
import collection.views as collection_views
import user.views as user_views
import search.views as search_views
# import predict.views as predict_views
from means.views import error_404, error_400, error_403, error_500

handler404 = error_404
handler400 = error_400
handler403 = error_403
handler500 = error_500

urlpatterns = [
    # main
    path('admin/', admin.site.urls),
    # path('', main_views.home, name="home"),
    # path('home/', main_views.home, name="home"),
    path('error_404/', main_views.error_404, name="error_404"),
    path('error_400/', main_views.error_400, name="error_400"),
    path('error_403/', main_views.error_403, name="error_403"),
    path('error_500/', main_views.error_500, name="error_500"),
    path('error_404_clean/', main_views.error_404_clean, name="error_404_clean"),
    path('error_400_clean/', main_views.error_400_clean, name="error_400_clean"),
    path('error_403_clean/', main_views.error_403_clean, name="error_403_clean"),
    path('error_500_clean/', main_views.error_500_clean, name="error_500_clean"),
    path('error_not_accessible/', main_views.error_not_accessible, name="error_not_accessible"),
    path('error_too_frequent/', main_views.error_too_frequent, name="error_too_frequent"),
    path('error_same_operation/', main_views.error_same_operation, name="error_same_operation"),
    path('release_show/', main_views.release_show, name="release_show"),
    path('copyright_show/', main_views.copyright_show, name="copyright_show"),
    path('agreement_show/', main_views.agreement_show, name="agreement_show"),

    # search
    path('search/', search_views.search, name="search"),
    path('search_pan/', search_views.search_pan, name='search_pan'),
    re_path(r'search_pan/declare/(.+)/(.+)/(.+)$', search_views.show_declare_pan, name='show_declare_pan'),
    path('search_pan/jump/', search_views.jump_to_pan, name='jump_to_pan'),
    path('search_magnet/', search_views.search_magnet, name='search_magnet'),
    re_path(r'search_magnet/details/(.+)/(.+)$', search_views.show_details_magnet, name='show_details_magnet'),
    path('search_movie/', search_views.search_movie, name='search_movie'),
    path('search_movie/details/', search_views.show_details_movie, name='show_details_movie'),

    # predict
    # path('pwi/', predict_views.predict_words_inner, name='predict_words_inner'),
    # path('predict_words_inner_atp_image/', predict_views.predict_words_inner_atp_image, name='predict_words_inner_atp_image'),
    # path('submit_atp/', predict_views.submit_atp, name='submit_atp'),
    # path('generate/', predict_views.generate, name='generate'),
    # path('generate/generate_honeyed_words', predict_views.generate_honeyed_words, name='generate_honeyed_words'),

    # user
    re_path('^login/$', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('register/', user_views.register, name="register"),
    path('user_setting/', user_views.user_setting, name="user_setting"),
    path('change_password/', user_views.change_password, name="change_password"),
    path('check_username_validate/', user_views.check_username_validate, name="check_username_validate"),
    path('check_password_validate/', user_views.check_password_validate, name="check_password_validate"),
    path('check_old_password_validate/', user_views.check_old_password_validate, name="check_old_password_validate"),
    path('check_password_repeat_validate/', user_views.check_password_repeat_validate, name="check_password_repeat_validate"),
    path('check_lastname_validate/', user_views.check_lastname_validate, name="check_lastname_validate"),
    path('check_firstname_validate/', user_views.check_firstname_validate, name="check_firstname_validate"),
    path('check_email_validate/', user_views.check_email_validate, name="check_email_validate"),
    path('check_question_validate/', user_views.check_question_validate, name="check_question_validate"),
    path('check_answer_validate/', user_views.check_answer_validate, name="check_answer_validate"),
    path('check_post_valudate/', user_views.check_post_valudate, name="check_post_valudate"),
    path(r'set_email_verify/', user_views.set_email_verify, name="set_email_verify"),
    path(r'send_set_user_verify_email/', user_views.send_set_user_verify_email, name="send_set_user_verify_email"),
    path(r'pre_reset_password/', user_views.pre_reset_password, name="pre_reset_password"),
    path(r'pre_reset_password_by_email/', user_views.pre_reset_password_by_email, name="pre_reset_password_by_email"),
    path(r'send_reset_password_email/', user_views.send_reset_password_email, name="send_reset_password_email"),
    re_path(r'check_set_user_verify_email/(.*)/$', user_views.check_set_user_verify_email, name="check_set_user_verify_email"),
    re_path(r'reset_password_by_email/(.*)/$', user_views.reset_password_by_email, name="reset_password_by_email"),
    path('feedback/', user_views.feedback, name="feedback"),

    # collection
    path('', collection_views.collection, name="collection"),
    re_path(r'collection/collection_details/(.*)/$', collection_views.collection_details, name="collection_details"),
    path('collection/rate/', collection_views.rate, name='collection_rate'),
    path('collection/rate/comment/', collection_views.comment, name='collection_rate_comment'),
]
