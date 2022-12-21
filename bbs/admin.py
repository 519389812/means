from django.contrib import admin
from bbs.models import Classification, Type, Post


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    # change_list_template = "admin/change_list_with_richtext.html"
    list_display = ('id', 'classification', 'type', 'title', 'user', "update_datetime", "parent_post", "related_post")
    search_fields = ('title', 'user')
    list_filter = ('classification', 'type')


admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Post, PostAdmin)
