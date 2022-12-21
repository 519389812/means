from django.contrib import admin
from collection.models import Classification, Collection, Rate, Recommendation, Comment
from nanoid import generate
from means.settings import CODE_SIZE, CODE_STRING



class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_with_richtext.html"
    list_display = ('id', 'uuid', 'classification', 'title', 'update_datetime')
    search_fields = ('title', 'uuid')
    list_filter = ('classification',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not change:
                uuid = generate(CODE_STRING, CODE_SIZE)
                obj.uuid = uuid
            super().save_model(request, obj, form, change)


class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'user', 'score', 'create_datetime')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rate', 'user', 'create_datetime')


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'url', 'create_datetime')


admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
