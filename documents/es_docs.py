from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from documents.models import App, Game


@registry.register_document
class AppDocument(Document):
    class Index:
        name = "Apps"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = App

        fields = [
            "name",
            "paid",
        ]

        queryset_pagination = 5000


@registry.register_document
class GameDocument(Document):
    class Index:
        name = "Games"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Game

        fields = [
            "name",
            "paid",
        ]

        queryset_pagination = 5000
