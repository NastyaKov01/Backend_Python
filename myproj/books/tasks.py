from celery import shared_task
from django.core.mail import mail_admins
from books.models import Book

@shared_task
def mail_to_admin():
    mail_admins(subject="Test", message="Object was created.")
    return "Sent"

@shared_task
def count_books():
    num = len(Book.objects.all())
    with open("/home/anastasia/backend_python/Backend_Python/myproj/books/counts.txt", "a") as file:
        file.write(f"Number of books: {num}\n")
    return "Written"