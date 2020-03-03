from django.contrib import admin

from app.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    @staticmethod
    def post_title(obj):
        return obj.post.title

    list_display = ('category', 'title', 'slug', 'status', 'updated',
                    'publication_date', 'author', )
    fields = ('category', 'title', 'slug', 'author', 'status', 'content',
              'updated', 'publication_date')

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    @staticmethod
    def category_title(obj):
        return obj.post.name

    list_display = ('name', 'slug', 'comment', )
    fields = ('name', 'slug', 'comment', )

    prepopulated_fields = {"slug": ("name",)}
