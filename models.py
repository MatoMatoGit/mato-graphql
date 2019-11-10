from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship


class Sensor(Base):
    __tablename__ = 'sensors'
    uuid = Column(Integer, primary_key=True)
    hash = Column(String(16), index=True)


class Measurement(Base):
    __tablename__ = 'measurements'
    uuid = Column(Integer, primary_key=True)
    data = Column(Integer, index=True)
    created_on = Column(DateTime, default=func.now())
    sensor_hash = Column(String(16), ForeignKey('sensors.hash'))

    sensor = relationship(
        Sensor,
        backref=backref('sensors',
                        uselist=True,
                        cascade='delete,all'))
