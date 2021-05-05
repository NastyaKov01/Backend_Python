from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from genres.models import Genre

@require_GET
def get_list(request):
    genres = Genre.objects.all()
    data = [{"id": genre.id, "Название жанра": genre.name} for genre in genres]
    return JsonResponse({"Жанры": data})

@require_GET
def get_details(request, id):
    try:
        genre = Genre.objects.get(id=id)
    except Genre.DoesNotExist:
        return JsonResponse({"status": "404 страница не найдена"})
    books = [book.title for book in genre.book_set.all()]
    gnr = {"id": genre.id,
           "Название жанра": genre.name,
           "Книги этого жанра": books}
    return JsonResponse(gnr)

@csrf_exempt
@require_POST
def create(request):
    genre = request.POST
    if Genre.objects.filter(name=genre.get("name")).exists():
        return JsonResponse({"status": "406 Такой жанр уже существует"})
    new_genre = Genre.objects.create(name=genre.get("name"))
    return JsonResponse({"status": "201 Новый жанр добавлен", "id": new_genre.id})