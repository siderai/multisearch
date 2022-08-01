import graphene

import users.schema
import documents.schema


class Query(
    users.schema.Query,
    documents.schema.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    users.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
