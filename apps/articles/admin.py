from django.contrib import admin
from  .models import Tag,Post,Category
from .models import Comment

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','crated_at')
    list_filter = ('crated_at','updated_at','tag')
    search_fields = ('title',)
    readonly_fields = ('crated_at','updated_at')
    prepopulated_fields = ({'slug': ('title',)})
    filter_horizontal = ('tag',)



admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)


admin.site.register(Comment)
# Register your models here.
