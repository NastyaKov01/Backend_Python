from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from users.models import User
from books.models import Book

@require_GET
def get_list(request):
    users = User.objects.all()
    data = [{"id": user.id,
             "Фамилия пользователя": user.lastname,
             "Имя пользователя": user.firstname}
            for user in users]
    return JsonResponse({"Пользователи": data})

@require_GET
def get_details(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({"status": "404 страница не найдена"})
    books = [book.title for book in user.book.all()]
    usr = {"id": user.id,
           "Фамилия пользователя": user.lastname,
           "Имя пользователя": user.firstname,
           "Книги, купленные этим пользователем": books}
    return JsonResponse(usr)

@csrf_exempt
@require_POST
def create(request):
    user = request.POST
    if User.objects.filter(lastname=user.get("lastname")).exists():
        return JsonResponse({"status": "406 Такой пользователь уже существует"})
    new_user = User.objects.create(lastname=user.get("lastname"), firstname=user.get("firstname"))
    for curbook in user.get("books").split(","):
        if curbook.startswith(" "):
            curbook = curbook[1:]
        if curbook.endswith(" "):
            curbook = curbook[:-1]
        try:
            book = Book.objects.get(title=curbook)
        except Book.DoesNotExist:
            book = Book.objects.create(title=curbook)
        new_user.book.add(book)
    new_user.save()
    return JsonResponse({"status": "201 Новый пользователь добавлен", "id": new_user.id})