"""Testing database connection without async and using sqlalchemy sync engine."""
import sys
from uuid import UUID, uuid4

from sqlmodel import create_engine, Field
from sqlalchemy import URL

from backend.common.log import logger
from backend.core.config import settings


test_logger=logger.info(f'Create database engine: {settings.DB_ECHO}')
