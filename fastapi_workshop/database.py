from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    url="sqlite:///./workshop_db.db",
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,

)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    with db:
        try:
            yield db
        finally:
            db.close()
