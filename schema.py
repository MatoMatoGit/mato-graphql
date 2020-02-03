from models import Sensor as SensorModel, Measurement as MeasurementModel
from database import db_session, Base, engine

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
    sensors = SQLAlchemyConnectionField(Sensor)
    measurements = SQLAlchemyConnectionField(Measurement)


class CreateMeasurement(graphene.Mutation):
    class Arguments:
        sensor_hash = graphene.String(required=True)
        created_on_module = graphene.String(required=True)
        sensor_type = graphene.String(required=True)
        data = graphene.Float(required=True)

    sensor = graphene.Field(lambda: Sensor)
    measurement = graphene.Field(lambda: Measurement)

    def mutate(
            self,
            info,
            data,
            sensor_hash,
            created_on_module,
            sensor_type
    ):
        sensor = SensorModel(
            sensor_hash=sensor_hash,
            created_on_module=created_on_module
        )

        measurement = MeasurementModel(
            sensor_hash=sensor_hash,
            sensor_type=sensor_type,
            data=data,
            created_on_module=created_on_module
        )

        Base.metadata.create_all(engine)

        db_session.add(measurement)

        if not sensor.query.filter_by(sensor_hash=sensor_hash).first():
            db_session.add(sensor)

        db_session.commit()

        return CreateMeasurement(sensor=sensor, measurement=measurement)


class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()


schema = graphene.Schema(query=Query, types=[Sensor, Measurement], mutation=Mutation)
