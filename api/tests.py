from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from datetime import date

# Test custom validation for BookSerializer
class BookSerializerValidationTests(TestCase):
    def test_publication_year_not_in_future(self):
        current_year = date.today().year
        author = Author.objects.create(name='Test Author')

        # Attempt to create book with future year
        client = APIClient()
        data = {
            'title': 'Future Book',
            'publication_year': current_year + 1,
            'author': author.id
        }
        response = client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)

# Test CRUD and filtering/search/ordering
class APICrudTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Jane Test')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )

    def test_get_author_with_books(self):
        response = self.client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Test')
        self.assertIsInstance(response.data['books'], list)
        self.assertGreaterEqual(len(response.data['books']), 1)

    def test_book_filtering_search_ordering(self):
        # Create extra book to test ordering & filtering
        Book.objects.create(title='Another Book', publication_year=2018, author=self.author)

        # Filtering by publication_year
        response = self.client.get('/api/books/?publication_year=2018')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for item in response.data['results']:
            self.assertEqual(item['publication_year'], 2018)

        # Searching by title
        response = self.client.get('/api/books/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Test Book' in b['title'] for b in response.data['results']))

        # Ordering by publication_year ascending
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data['results']]
        self.assertEqual(years, sorted(years))
