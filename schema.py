from models import Sensor as SensorModel, define_table_name
from database import db_session, Base, engine

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


class Sensor(SQLAlchemyObjectType):
    class Meta:
        model = SensorModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_sensors = SQLAlchemyConnectionField(Sensor)


class CreateMeasurement(graphene.Mutation):
    class Arguments:
        data = graphene.Int(required=True)
        sensor_hash = graphene.String(required=True)

    sensor = graphene.Field(lambda: Sensor)

    def mutate(self, info, data, sensor_hash):
        measurement_model = define_table_name(sensor_hash)
        measurement = measurement_model(data=data, sensor_hash=sensor_hash)
        sensor = SensorModel(sensor_hash=sensor_hash)

        Base.metadata.create_all(engine)

        db_session.add(measurement)

        if not sensor.query.filter_by(sensor_hash=sensor_hash).first():
            db_session.add(sensor)

        db_session.commit()

        return CreateMeasurement(sensor=sensor)


class Mutation(graphene.ObjectType):
    create_measurement = CreateMeasurement.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
