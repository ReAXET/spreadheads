"""API Routers"""
from typing import List, Optional, Union, Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from backend.common.log import log
from backend.database.core import get_session
from backend.models.nba.teams_model import NBATeam
from backend.models.nba.players_model import NBAPlayer
from backend.schemas.nba.teams_schema import NBATeamSchema, NBATeamSchemaCreate, NBATeamSchemaUpdate
from backend.schemas.nba.players_schema import NBAPlayerSchema, NBAPlayerSchemaCreate, NBAPlayerSchemaUpdate

router = APIRouter()


@router.get('/all', summary="Get all information for the API", dependencies=[DependsJWTAuth])   