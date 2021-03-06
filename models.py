from sqlalchemy import \
    Integer, \
    Column, \
    DateTime, \
    String, \
    func, \
    Float
from database import Base


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    sensor_hash = Column(String(32), nullable=False, index=True)
    created_on_module = Column(String(128))
    created_on_server = Column(DateTime, default=func.now())
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return '<Sensor model {}>'.format(self.id)


class Measurement(Base):
    __tablename__ = 'measurements'
    uuid = Column(Integer, primary_key=True)
    sensor_hash = Column(String(32), nullable=False, index=True)
    sensor_type = Column(String(32), nullable=False, index=True)
    data = Column(Float, nullable=False, index=True)
    created_on_module = Column(String(128))
    created_on_server = Column(DateTime, default=func.now())
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return '<Measurement model {}>'.format(self.uuid)
