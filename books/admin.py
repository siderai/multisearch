from django.contrib import admin

from books.models import Book, Document

admin.site.register(Book)
admin.site.register(Document)
