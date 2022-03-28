from django.shortcuts import render
# Create your views here.
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        "books":books
    })

def book_detail(request, slug):
    books = Book.objects.get(slug = slug)
    return render(request, 'book_outlet/book_detail.html', {
        "title": books.title,
        "author": books.author,
        "rating":books.rating,
        "is_bestselling": books.is_bestselling,
        "slug":books.slug
    })
