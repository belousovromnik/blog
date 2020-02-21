from django.contrib import admin
from app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    @staticmethod
    def post_title(obj):
        return obj.post.title

    list_display = ('title', 'slug', 'status', 'updated',
                    'publication_date', 'author', )
    fields = ('title', 'slug', 'author', 'status', 'content',
              'updated', 'publication_date')

    prepopulated_fields = {"slug": ("title",)}
