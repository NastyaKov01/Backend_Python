from django.http import JsonResponse
from django.shortcuts import render
from books.models import Book

if len(Book.objects.all()) == 0:
    book = Book.objects.create(title="Harry Potter", author="J.K.Rowling",
                                   year=1997, price=45)
    book = Book.objects.create(title="The Lord of the Rings", author="John R.R.Tolkien",
                                   year=1948, price=50)
    book = Book.objects.create(title="The Chronicals of Narnia", author="C.S.Lewis",
                                   year=1950, price=60)
    book = Book.objects.create(title="Alice in Wonderland", author="Lewis Carroll",
                                   year=1865, price=57)

def create(request, book_title, book_author, pub_year, book_price):
    if request.method == "POST":
        book = Book.objects.create(title=book_title, author=book_author,
                                   year=pub_year, price=book_price)
        return JsonResponse({"Event": "New book added", "Book id": book.id, "status": 201})

def get_list(request):
    if request.method == "GET":
        return JsonResponse({'data': [{'id': book.id, 'status': book.title} for book in Book.objects.all()]})

def get_details(request, book_id):
    if request.method == "GET":
        try:
            b = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return JsonResponse({"status": "No such book"})
        return JsonResponse({'Book id': b.id, 'Title': b.title, 'Author': b.author,
                             'Year of first publication': b.year, 'Price': b.price})

def index(request):
    return render(request, 'books/index.html')