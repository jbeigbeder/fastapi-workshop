"""database configuration"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(url="sqlite:///./workshop_db.db",
                       connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()


def get_db():
    """get a database session that will be close at the end"""
    db = SessionLocal()

    with db:
        try:
            yield db
        finally:
            db.close()
