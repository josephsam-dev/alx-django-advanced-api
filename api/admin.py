from django.contrib import admin
from .models import Author, Book

# Register your models to appear in Django admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    search_fields = ('title',)
    list_filter = ('publication_year', 'author')
