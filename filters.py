from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from models import Sensor, Measurement


class SensorFilter(FilterSet):
    class Meta:
        model = Sensor
        fields = {
            'sensor_hash': ['eq', 'ne', 'in', 'ilike'],
        }


class MeasurementFilter(FilterSet):
    class Meta:
        model = Measurement
        fields = {
            'sensor_hash': ['eq', 'ne', 'in', 'ilike'],
            'sensor_type': ['eq', 'ne', 'in', 'ilike'],
        }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {Sensor: SensorFilter(), Measurement: MeasurementFilter()}
