from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorListCreateAPIView, AuthorRetrieveAPIView, BookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-detail'),
path('', include(router.urls)),
]