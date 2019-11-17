from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base

engine = create_engine('mysql+pymysql://root:admin123@localhost:3306/mato',
                       convert_unicode=True,
                       pool_size=10,
                       max_overflow=20,
                       echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def test_db():
    connection = engine.connect()

    result = connection.execute("select hash from sensor")
    for row in result:
        print("hash:", row['hash'])

    connection.close()
