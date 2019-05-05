from rest_framework import serializers
from .models import Book, BookInstance, Author, Genre, EndPointTest


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary',
                 'isbn', 'genre', 'date_of_publication',
                 'date_of_entry', 'total_books')


class BookInstanceSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookInstance
        fields = ('id', 'book', 'imprint', 'due_back', 'status')


class EndPointTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPointTest
        fields = '__all__'







