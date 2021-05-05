from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from authors.models import Author

@require_GET
def get_list(request):
    authors = Author.objects.all()
    data = [{"id": author.id, "Имя автора": author.name} for author in authors]
    return JsonResponse({"Авторы": data})

@require_GET
def get_details(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return JsonResponse({"status": "404 страница не найдена"})
    books = [book.title for book in author.book_set.all()]
    auth = {"id": author.id,
           "Имя автора": author.name,
           "Книги этого автора": books}
    return JsonResponse(auth)

@csrf_exempt
@require_POST
def create(request):
    author = request.POST
    if Author.objects.filter(name=author.get("name")).exists():
        return JsonResponse({"status": "406 Такой автор уже существует"})
    new_author = Author.objects.create(name=author.get("name"))
    return JsonResponse({"status": "201 Новый автор добавлен", "id": new_author.id})