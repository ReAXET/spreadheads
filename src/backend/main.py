"""Main module for the backend to create all tables and run the FastAPI server."""
import sys
from typing import Optional
from uuid import UUID, uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import create_engine, Field
from sqlalchemy import URL

from backend.common.log import log
from backend.core.config import settings
from backend.database.test_connection import create_table, drop_table
from backend.models.base_models import Base
from backend.routers import nba