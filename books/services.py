from .models import Book
from django.core.exceptions import ObjectDoesNotExist

class BookService:
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book_by_id(book_id):
        try:
            return Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_book(data):
        return Book.objects.create(**data)

    @staticmethod
    def update_book(book_id, data):
        try:
            book = Book.objects.get(id=book_id)
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return book
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def delete_book(book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return True
        except ObjectDoesNotExist:
            return False