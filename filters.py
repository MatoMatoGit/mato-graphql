from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from models import Sensor, Measurement


class SensorFilter(FilterSet):
    class Meta:
        model = Sensor
        fields = {
            'sensor_hash': ['eq']
        }


class MeasurementFilter(FilterSet):
    class Meta:
        model = Measurement
        fields = {
            'sensor_hash': ['eq'],
            'sensor_type': ['eq']
        }


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {Sensor: SensorFilter(), Measurement: MeasurementFilter()}
