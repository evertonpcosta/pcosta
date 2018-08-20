import leads_api.leads.schema
from leads_api.leads.models import Pessoa, Tipo
import graphene

from graphene_django.debug import DjangoDebug


class Query(leads_api.leads.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(leads_api.leads.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
