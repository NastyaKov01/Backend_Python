from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from books.models import Book
from genres.models import Genre
from authors.models import Author

@csrf_exempt
@require_POST
def create(request):
    book = request.POST
    if Book.objects.filter(title=book.get("title")).exists():
        return JsonResponse({"status": "Такая книга уже существует"}, status=406)
    b_auth = book.get("author")
    new_book = Book.objects.create(
                title=book.get("title"),
                year=book.get("year"),
                price=book.get("price"))
    try:
        auth = Author.objects.get(name=b_auth)
    except Author.DoesNotExist:
        auth = Author.objects.create(name=b_auth)
    new_book.author = auth
    for gnr in book.get("genre").split(","):
        if gnr.startswith(" "):
            gnr = gnr[1:]
        if gnr.endswith(" "):
            gnr = gnr[:-1]
        try:
            genre = Genre.objects.get(name=gnr)
        except Genre.DoesNotExist:
            genre = Genre.objects.create(name=gnr)
        new_book.genre.add(genre)
    new_book.save()
    return JsonResponse({"status": "201 Книга добавлена", "id": new_book.id}, status=201)

@require_GET
def get_list(request):
    books = Book.objects.all()
    data = [{"id": book.id, "Название": book.title} for book in books]
    return JsonResponse({"Список книг": data}, status=200)

@require_GET
def get_details(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return JsonResponse({"status": "страница не найдена"}, status=404)
    gnr = [genre.name for genre in book.genre.all()]
    res = {"id": book.id,
           "Название книги": book.title,
           "Автор книги": book.author.name,
           "Жанры книги": gnr,
           "Год публикации": book.year,
           "Цена": book.price}
    return JsonResponse(res, status=200)

@csrf_exempt
@require_http_methods(["DELETE"])
def remove(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return JsonResponse({"status": "Книга не найдена"}, status=404)
    book.delete()
    return JsonResponse({"result":"Книга удалена"}, status=200)

@csrf_exempt
@require_http_methods(["PUT"])
def change(request, id):
    params = dict()
    string = request.readline()
    while string != b"":
        tmp = string.decode('utf-8').split(":")
        if len(tmp) != 1:
            params[tmp[0]] = tmp[1].replace("\n", "")
        string = request.readline()
    print(params)
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return JsonResponse({"status": "Книга не найдена"}, status=404)
    print(book)
    book.title = params["title"]
    b_auth = params["author"]
    book.year = params["year"]
    book.price = params["price"]
    try:
        auth = Author.objects.get(name=b_auth)
    except Author.DoesNotExist:
        auth = Author.objects.create(name=b_auth)
    book.author = auth
    for gnr in book.genre.all():
        book.genre.remove(gnr)
    for gnr in params["genre"].split(","):
        if gnr.startswith(" "):
            gnr = gnr[1:]
        if gnr.endswith(" "):
            gnr = gnr[:-1]
        try:
            genre = Genre.objects.get(name=gnr)
        except Genre.DoesNotExist:
            genre = Genre.objects.create(name=gnr)
        book.genre.add(genre)
    book.save()
    return JsonResponse({"status":"Книга изменена"}, status=200)

@require_GET
def index(request):
    return render(request, 'books/index.html')

# books = [{"id":1, "title":"Гарри Поттер", "author":"Дж.К.Роулинг", "year":1997, "price":45},
#         {"id":2, "title":"Властилин колец", "author":"Дж.Р.Р.Толкин", "year":1948, "price":50},
#         {"id":3, "title":"Хроники Нарнии", "author":"К.С.Льюис", "year": 1950, "price": 60},
#         {"id":4, "title":"Алиса в Стране чудес", "author":"Л.Кэрролл", "year":1865, "price": 55}]
#
# @csrf_exempt
# def create(request):
#    if request.method == "POST":
#         book = {"id": request.POST.get("id"), "title": request.POST.get("title"), "author": request.POST.get("author"),
#             "year": request.POST.get("year"), "price": request.POST.get("price")}
#         try:
#             book["id"] = int(book["id"])
#             book["year"] = int(book["year"])
#             book["price"] = int(book["price"])
#         except ValueError:
#             return JsonResponse({"status": "404 страница не найдена"})
#         if type(book["id"]) == int and type(book["title"]) == str and type(book["author"]) == str \
#                     and type(book["year"]) == int and type(book["price"]) == int:
#             books.append(book)
#             return JsonResponse({"Event": "Новая книга добавлена", "status": 201})
#    return JsonResponse({"status": "404 страница не найдена"})
#
# def get_list(request):
#     if request.method == "GET":
#         return JsonResponse({"data": [{"id": book["id"], "status": book["title"]} for book in books]})
#     return JsonResponse({"status": "404 страница не найдена"})
#
# def get_details(request, id):
#     if request.method == "GET":
#         found_book = 0
#         for book in books:
#             if book["id"] == id:
#                 found_book = book
#         if found_book != 0:
#             return JsonResponse({'ID книги': found_book["id"], 'Название книги': found_book["title"],
#                         'Автор': found_book["author"], 'Год публикации': found_book["year"],
#                         'Цена': found_book["price"]})
#         return JsonResponse({"status": "404 станица не найдена"})
#     return JsonResponse({"status": "404 страница не найдена"})
#
# def index(request):
#     if request.method == "GET":
#         return render(request, 'books/index.html')
#     return JsonResponse({"status": "404 страница не найдена"})