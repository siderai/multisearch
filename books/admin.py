from django.contrib import admin

from books.models import Book, Document

# Register your models here.
admin.site.register(Book)
admin.site.register(Document)
