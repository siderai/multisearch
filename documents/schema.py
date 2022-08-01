import graphene
from graphene_django import DjangoListField, DjangoObjectType

from documents.models import App, Game
from documents.search import search


class GameType(DjangoObjectType):
    class Meta:
        model = Game
        fields = ("id", "name", "paid")


class AppType(DjangoObjectType):
    class Meta:
        model = App
        fields = ("id", "name", "paid")


class Query(graphene.ObjectType):
    free_apps = DjangoListField(AppType)
    all_apps = DjangoListField(AppType)

    free_games = DjangoListField(GameType)
    all_games = DjangoListField(GameType)

    @classmethod
    def get_queryset(cls, queryset, info):
        if info.context.user.is_authenticated:
            return queryset
        return queryset.none()

    def resolve_all_apps(root, info):
        if info.context.user.paid:
            return App.objects.all()
        return App.objects.filter(paid=False)

    def resolve_all_Games(root, info):
        if info.context.user.paid:
            return App.objects.all()
        return App.objects.filter(paid=False)


schema = graphene.Schema(query=Query)
