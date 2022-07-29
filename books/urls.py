from django.conf.urls import url
from graphene_django.views import GraphQLView

from books.schema import schema

urlpatterns = [
    url("", GraphQLView.as_view(graphiql=True, schema=schema)),
]
