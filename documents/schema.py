import graphene
from graphene_django import DjangoListField, DjangoObjectType
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from documents.models import App, Game
from documents.es_docs import AppDocument, GameDocument
from documents.exceptions import (
    DjangoElasticsearchDslError,
)  # not implemented yet, todo


client = Elasticsearch()


class GameType(DjangoObjectType):
    class Meta:
        model = Game
        fields = ("id", "name", "paid")

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_authenticated:
            if info.context.user.paid:
                return queryset
            return queryset.filter(paid=False)
        return queryset.none()


class AppType(DjangoObjectType):
    class Meta:
        model = App
        fields = ("id", "name", "paid")

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_authenticated:
            if info.context.user.paid:
                return queryset
            return queryset.filter(paid=False)
        return queryset.none()


class Query(graphene.ObjectType):
    find_all_apps = DjangoListField(AppType, search_string=graphene.String())
    find_all_games = DjangoListField(GameType, search_string=graphene.String())

    def resolve_all_apps(self, info, search_string):
        request = AppDocument.search(using=client).query(
            "match", name=f"{search_string}"
        )
        try:
            response = request.execute()
            qs = response.to_queryset()
            return qs
        except DjangoElasticsearchDslError:
            pass

    def resolve_all_games(self, info, search_string):
        request = GameDocument.search(using=client).query(
            "match", name=f"{search_string}"
        )
        try:
            response = request.execute()
            qs = response.to_queryset()
            return qs
        except DjangoElasticsearchDslError:
            pass


schema = graphene.Schema(query=Query)
