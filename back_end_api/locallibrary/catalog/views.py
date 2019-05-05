from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.views import generic
from .models import Book, BookInstance, Author, Genre, EndPointTest
from rest_framework import generics
from .serializers import BookInstanceSerializer, BookSerializer, GenreSerializer, AuthorSerializer, EndPointTestSerializer


# Create your views here.
def index(request):
    return render(
        request,
        'chart.html'
    )

def country(request):
    return render(
        request,
        'countries.html'
    )

def index2(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


# BookDetailView
class BookDetailView(generic.DetailView):
    model = Book


# BookListView
class BookListView(generic.ListView):
    model = Book


class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        """
        Return a list of all books.
        """
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response({'data':serializer.data})


class BookListDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class EndPointTestListAPIView(generics.ListCreateAPIView):
    queryset = EndPointTest.objects.all()
    serializer_class = EndPointTestSerializer

    def get(self, request):
        """
        Return a list of all entries.
        """
        queryset = EndPointTest.objects.all()
        serializer = EndPointTestSerializer(queryset, many=True)
        return Response({'data':serializer.data})

    # def post(self, request):
    #     article = request.data.get('free_text')

    #     # Create an article from the above data
    #     serializer = EndPointTestSerializer(data=article)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' created successfully".format(article_saved.free_text)})