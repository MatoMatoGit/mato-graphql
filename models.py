from sqlalchemy import *
from database import Base


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    sensor_hash = Column(String(16))
    created_on_server = Column(DateTime, default=func.now())
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return '<Sensor model {}>'.format(self.id)


def define_table_name(hash_table_name):
    class Measurement(Base):
        __tablename__ = hash_table_name
        uuid = Column(Integer, primary_key=True)
        data = Column(Integer, index=True)
        sensor_hash = Column(String(16))
        created_on_server = Column(DateTime, default=func.now())
        __table_args__ = {'extend_existing': True}

        def __repr__(self):
            return '<Measurement model {}>'.format(self.uuid)

    return Measurement
