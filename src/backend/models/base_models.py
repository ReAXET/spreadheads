"""Base Model for all existing models."""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from pydantic_settings import SettingsConfigDict
from sqlalchemy.orm import declared_attr

from backend.common.log import log

class Base(SQLModel, table=True):
    """Base Model for all existing models."""

    model_config = SettingsConfigDict(extra="allow", from_attributes=True, arbitrary_types_allowed=True, env_file='.env', env_file_encoding='utf-8')
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = Field(default=None, nullable=True)

    @declared_attr.directive

    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    @declared_attr.directive
    def __table_args__(cls) -> dict:
        return {'extend_existing': True}
    
    @declared_attr.directive
    def __mapper_args__(cls) -> dict:
        return {'eager_defaults': True}
    
    @declared_attr.directive
    def __repr__(cls) -> str:
        return f'<{cls.__name__} {cls.id}>'
    
    

