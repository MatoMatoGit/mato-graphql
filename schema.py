# GraphQL
import graphene
from graphene import Connection, Node
from graphene_sqlalchemy import SQLAlchemyObjectType

# Project
from models import Sensor as SensorModel, Measurement as MeasurementModel
from database import db_session, Base, engine
from filters import MyFilterableConnectionField


class SensorNode(SQLAlchemyObjectType):
    class Meta:
        model = SensorModel
        interfaces = (Node,)
        connection_field_factory = MyFilterableConnectionField.factory


class SensorConnection(Connection):
    class Meta:
        node = SensorNode


class MeasurementNode(SQLAlchemyObjectType):
    class Meta:
        model = MeasurementModel
        interfaces = (Node,)
        connection_field_factory = MyFilterableConnectionField.factory


class MeasurementConnection(Connection):
    class Meta:
        node = MeasurementNode


class Query(graphene.ObjectType):
    sensor = graphene.relay.Node.Field(SensorNode)
    all_sensors = MyFilterableConnectionField(SensorConnection)

    measurement = graphene.relay.Node.Field(MeasurementNode)
    all_measurements = MyFilterableConnectionField(MeasurementConnection)


class CreateMeasurement(graphene.Mutation):
    class Arguments:
        sensor_hash = graphene.String(required=True)
        created_on_module = graphene.String(required=True)
        sensor_type = graphene.String(required=True)
        data = graphene.Float(required=True)

    sensor = graphene.Field(lambda: SensorNode)
    measurement = graphene.Field(lambda: MeasurementNode)

    @staticmethod
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


schema = graphene.Schema(query=Query, mutation=Mutation)
