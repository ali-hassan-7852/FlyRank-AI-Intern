from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from SRC.utils.settings import setting

Base = declarative_base()

engine = create_engine(url=setting.DB_connection)

localsession = sessionmaker(bind=engine)

def get_db():
    session = localsession()
    try:
        yield session

    finally:
        session.close()
        