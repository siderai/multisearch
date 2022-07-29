import django
import graphene
from attr import field
from graphene_django import DjangoListField, DjangoObjectType

from books.models import Book, Document


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "excerpt")


class DocumentType(DjangoObjectType):
    class Meta:
        model = Document
        fields = ("id", "name", "paid")


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    free_docs = DjangoListField(DocumentType)
    all_docs = DjangoListField(DocumentType)

    def resolve_all_books(root, info):
        return Book.objects.filter(title="django")

    def resolve_free_docs(root, info):
        return Document.objects.filter(paid=False)

    def resolve_all_docs(root, info):
        return Document.objects.all()


schema = graphene.Schema(query=Query)
