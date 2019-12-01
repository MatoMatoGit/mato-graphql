from models import Sensor as SensorModel, Measurement as MeasurementModel
from database import db_session

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


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
        hash = graphene.String(required=True)

    measurement = graphene.Field(lambda: Measurement)
    sensor = graphene.Field(lambda: Sensor)

    def mutate(self, info, data, hash):
        measurement = MeasurementModel(data=data)
        sensor = SensorModel(hash=hash)
        db_session.add(measurement)
        db_session.add(sensor)
        db_session.commit()

        return CreateMeasurement(measurement=measurement, sensor=sensor)


class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Measurement, Sensor])
