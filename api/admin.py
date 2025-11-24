from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
