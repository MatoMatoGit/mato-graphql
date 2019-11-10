from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://root:admin123@localhost:3306/mato',
                       convert_unicode=True,
                       pool_size=10,
                       max_overflow=20)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import Sensor, Measurement
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    test_sensor = Sensor(hash='AAAA00')
    db_session.add(test_sensor)

    test_measurement = Measurement(data=12, sensor=test_sensor)
    db_session.add(test_measurement)
    db_session.commit()


def test_db():
    connection = engine.connect()

    result = connection.execute("select hash from sensors")
    for row in result:
        print("hash:", row['hash'])

    connection.close()
