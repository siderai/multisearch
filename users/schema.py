import graphene
from graphql_auth import mutations
from graphql_auth.schema import MeQuery, UserQuery


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail()
    send_password_reset_email = mutations.SendPasswordResetEmail()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    # graphene_auth provides user endpoints here
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
