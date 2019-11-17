from models import Sensor as SensorModel
from models import Measurement as MeasurementModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class Sensor(SQLAlchemyObjectType):
    class Meta:
        model = SensorModel
        interfaces = (relay.Node,)


class Measurement(SQLAlchemyObjectType):
    class Meta:
        model = MeasurementModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    measurement = graphene.Field(Measurement)


class CreateMeasurement(graphene.Mutation):
    class Arguments:
        uuid = graphene.ID()
        data = graphene.Int(required=True)
        hash = graphene.String(required=True)

    measurement = graphene.Field(lambda: Sensor)
    sensor = graphene.Field(lambda: Measurement)

    def mutate(self, info, data, hash):
        measurement = Measurement(data=data)
        sensor = Sensor(hash=hash)

        return CreateMeasurement(measurement=measurement, sensor=sensor)


class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
