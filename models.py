from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from database import Base


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    hash = Column(String(16))
    measurements = relationship('Measurement', backref="sensor", cascade="all, delete-orphan", lazy='dynamic')

    def __repr__(self):
        return '<Sensor model {}>'.format(self.id)


class Measurement(Base):
    __tablename__ = 'measurement'
    uuid = Column(Integer,
                  primary_key=True,
                  nullable=True)
    data = Column(Integer, index=True)
    created_on = Column(DateTime, default=func.now())
    sensor_id = Column(Integer, ForeignKey('sensor.id'))

    def __repr__(self):
        return '<Measurement model {}>'.format(self.uuid)
