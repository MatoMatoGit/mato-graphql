from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://root:admin123@localhost:3306/mato',
                       convert_unicode=True,
                       pool_size=10,
                       max_overflow=20,
                       echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import Sensor, Measurement
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    test_hash = "TEST00001"
    test_date = "2018-12-25 09:27:53"
    test_sensor = Sensor(
        sensor_hash=test_hash,
        created_on_module=test_date)
    db_session.add(test_sensor)
    test_measurement = Measurement(
        sensor_hash=test_sensor,
        sensor_type="temp",
        data=99,
        created_on_module=test_date)
    db_session.add(test_measurement)
    db_session.commit()


def test_db():
    connection = engine.connect()

    result = connection.execute("select sensor_hash from sensor")
    for row in result:
        print("sensor_hash:", row['sensor_hash'])

    connection.close()
