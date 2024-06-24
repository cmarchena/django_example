from django.contrib import admin
from .models import Post, Profile
def toggle_published(modeladmin, request, queryset):
    for post in queryset:
        post.status = 'draft' if post.status == 'published' else 'published' #Ternary operator
        post.save()
toggle_published.short_description = "Toggle selected stories status"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_display_links = ('title',)
    # list_editable = ('title',)
    list_filter = ('created_at', 'updated_at', 'status')
    search_fields = ('title', 'content')
    actions = [toggle_published]


admin.site.register(Profile)