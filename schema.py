from models import Sensor as SensorModel
from models import Measurement as MeasurementModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Sensor(SQLAlchemyObjectType):
    class Meta:
        model = SensorModel
        interfaces = (relay.Node,)


class Measurement(SQLAlchemyObjectType):
    class Meta:
        model = MeasurementModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_measurements = SQLAlchemyConnectionField(Measurement, sort=Measurement.sort_argument())
    all_sensors = SQLAlchemyConnectionField(Sensor, sort=None)


class CreateMeasurement(graphene.Mutation):
    class Arguments:
        data = graphene.Int(required=True)
        sensor_hash = graphene.String(required=True)

    measurement = graphene.Field(lambda: Measurement)

    def mutate(self, info, data, sensor_hash):
        measurement = Measurement(data=data, sensor_hash=sensor_hash)
        return CreateMeasurement(measurement=measurement)


class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Sensor, Measurement])
