from django.contrib import admin

# Register your models here.
from. models import HomePage,AboutPage,Post,Comment

admin.site.register(HomePage)
admin.site.register(AboutPage)

#######
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','created_at','status']
    list_filter = ['status','created_at','publish','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','created_at','active','body']
    list_filter = ['active','created_at']
    search_fields = ['name','body','body']
   