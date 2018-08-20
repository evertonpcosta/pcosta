import graphene
import base64
from leads_api.leads.models import Pessoa, Tipo
from graphene import AbstractType, Node, relay, String, Int, Field, ObjectType, Mutation
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class PessoaNode(DjangoObjectType):

    class Meta:
        model = Pessoa
        interfaces = (Node, )
        filter_fields = ['nome']


class TipoNode(DjangoObjectType):

    class Meta:
        model = Tipo
        interfaces = (Node, )
        filter_fields = ['nome']


class PessoaInput(graphene.InputObjectType):
    nome = String(required=True)
    email = String(required=True)
    telefone = String(required=True)
    cep = String(required=True)
    quantidade_vidas = String(required=True)
    id_pessoa_tipo = String(required=True)


class CreatePessoa(graphene.Mutation):
    class Arguments:
        pessoa_data = PessoaInput(required=True)

    pessoa = graphene.Field(PessoaNode)

    @staticmethod
    def mutate(root, info, pessoa_data=None):

        unbased_global_id = str(base64.b64decode(pessoa_data.id_pessoa_tipo))
        _id = unbased_global_id.split(':')[1]
        
        tipo_pessoa = Tipo.objects.get(id=_id.replace("'",''))
        pessoa = Pessoa(
            nome=pessoa_data.nome,
            email=pessoa_data.email,
            telefone=pessoa_data.telefone,
            cep=pessoa_data.cep,
            quantidade_vidas=pessoa_data.quantidade_vidas,
            pessoa_tipo=tipo_pessoa
        )

        pessoa.save()
        return CreatePessoa(pessoa=pessoa)


class Query(AbstractType):
    all_pessoas = DjangoFilterConnectionField(PessoaNode)

    def resolve_all_products(self, args, context, info):
        return Pessoa.objects.all()

    tipo = Node.Field(TipoNode)
    all_tipo = DjangoFilterConnectionField(TipoNode)

# Creating Schema


class Mutation(ObjectType):
    create_pessoa = CreatePessoa.Field()
