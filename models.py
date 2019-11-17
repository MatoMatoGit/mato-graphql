from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    hash = Column(String)

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

    sensor = relationship(
        Sensor,
        backref=backref('measurements',
                        uselist=True,
                        cascade='delete,all'))

    def __repr__(self):
        return '<Measurement model {}>'.format(self.uuid)
