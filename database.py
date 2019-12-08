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


def test_db():
    connection = engine.connect()

    result = connection.execute("select sensor_hash from sensor")
    for row in result:
        print("sensor_hash:", row['sensor_hash'])

    connection.close()
