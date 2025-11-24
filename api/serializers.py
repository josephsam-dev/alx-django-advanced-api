from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for the Book model
# Serializes all fields and validates that publication_year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure publication_year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (max {date.today().year})."
            )
        return value

# Serializer for the Author model
# Includes the name and a nested list of all related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
