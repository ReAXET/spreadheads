"""Testing database connection without async and using sqlalchemy sync engine."""
import sys
from uuid import UUID, uuid4

from sqlmodel import create_engine, Field
from sqlalchemy import URL

from backend.common.log import log
from backend.core.config import settings
from backend.models.base_models import Base



def create_test_engine_and_session(url: str | URL):
    try:
        engine = create_engine(url, echo=settings.DB_ECHO)
        logger.info(f'Create database engine: {url}')
    except Exception as e:
        logger.error(f'Create database engine failed: {e}')
        sys.exit(1)
    else:
        db_session = engine
        logger.info(f'Create database session: {url}')
        return engine, db_session
    

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
)

engine, db_session = create_test_engine_and_session(SQLALCHEMY_DATABASE_URL)

class TestTable(Base, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None, nullable=True)
    age: int = Field(default=None, nullable=True)
    class Config:
        table_name = 'test_table'
        from_attributes= True

def create_table():
    # Create the TestTable table
    TestTable.metadata.create_all(engine)
    logger.info(f'Create database table: {TestTable.metadata.tables.keys()}')

def drop_table():
    # Drop the TestTable table
    TestTable.metadata.drop_all(engine)
    logger.info(f'Drop database table: {TestTable.metadata.tables.keys()}')

