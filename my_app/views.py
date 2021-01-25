from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Author, Book, Genre
# Create your views here.


def index(request):
    context = {'write': "it's just your practice site"}
    return render(request, 'index.html', context=context)


def books(request):
    books = Book.objects.order_by('title')
    list_of_books = {'books_list': books}
    return render(request, 'books.html', context=list_of_books)
