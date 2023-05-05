from django.contrib import admin

from .models import Post,Category,Tags

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_date']
    list_filter = ['status']
    search_fields = ['status']
    empty_value_display = 'empty-value'
    
admin.site.register(Category)
admin.site.register(Tags)
