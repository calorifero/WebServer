import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import TemperatureModel, EspModel


class Esp(SQLAlchemyObjectType):
    class Meta:
        model = EspModel
        interfaces = (relay.Node,)


class Temperature(SQLAlchemyObjectType):
    class Meta:
        model = TemperatureModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_esp = SQLAlchemyConnectionField(Esp)


schema = graphene.Schema(query=Query)
