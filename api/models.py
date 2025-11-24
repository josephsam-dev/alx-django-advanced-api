from django.db import models

# Author model represents a book author.
# Each author can have multiple books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model represents a book written by an Author.
# Fields:
# - title: the title of the book
# - publication_year: year of publication
# - author: foreign key linking to the Author model
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
