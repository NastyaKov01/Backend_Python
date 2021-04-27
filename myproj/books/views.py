from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from books.models import Book

books = [{"id":1, "title":"Гарри Поттер", "author":"Дж.К.Роулинг", "year":1997, "price":45},
        {"id":2, "title":"Властилин колец", "author":"Дж.Р.Р.Толкин", "year":1948, "price":50},
        {"id":3, "title":"Хроники Нарнии", "author":"К.С.Льюис", "year": 1950, "price": 60},
        {"id":4, "title":"Алиса в Стране чудес", "author":"Л.Кэрролл", "year":1865, "price": 55}]

@csrf_exempt
def create(request):
   if request.method == "POST":
        book = {"id": request.POST.get("id"), "title": request.POST.get("title"), "author": request.POST.get("author"),
            "year": request.POST.get("year"), "price": request.POST.get("price")}
        try:
            book["id"] = int(book["id"])
            book["year"] = int(book["year"])
            book["price"] = int(book["price"])
        except ValueError:
            return JsonResponse({"status": "404 страница не найдена"})
        if type(book["id"]) == int and type(book["title"]) == str and type(book["author"]) == str \
                    and type(book["year"]) == int and type(book["price"]) == int:
            books.append(book)
            return JsonResponse({"Event": "Новая книга добавлена", "status": 201})
   return JsonResponse({"status": "404 страница не найдена"})

def get_list(request):
    if request.method == "GET":
        return JsonResponse({"data": [{"id": book["id"], "status": book["title"]} for book in books]})
    return JsonResponse({"status": "404 страница не найдена"})

def get_details(request, id):
    if request.method == "GET":
        found_book = 0
        for book in books:
            if book["id"] == id:
                found_book = book
        if found_book != 0:
            return JsonResponse({'ID книги': found_book["id"], 'Название книги': found_book["title"],
                        'Автор': found_book["author"], 'Год публикации': found_book["year"],
                        'Цена': found_book["price"]})
        return JsonResponse({"status": "404 станица не найдена"})
    return JsonResponse({"status": "404 страница не найдена"})

def index(request):
    if request.method == "GET":
        return render(request, 'books/index.html')
    return JsonResponse({"status": "404 страница не найдена"})