from django.contrib import admin
from user.models import User, EmailVerifyRecord, Feedback, Agreement, AgreementSignRecord
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'ip_address', 'last_login')
    filter_horizontal = ('groups', 'user_permissions', )


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'code', 'type', 'close_datetime')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'create_datetime')


class AgreementAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'title', 'must_sign', 'create_datetime')


class AgreementSignRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreement', 'user', 'create_datetime')


admin.site.register(User, CustomUserAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(AgreementSignRecord, AgreementSignRecordAdmin)

admin.site.site_header = '后台管理'
admin.site.site_title = '后台管理'
admin.site.index_title = '后台管理'
