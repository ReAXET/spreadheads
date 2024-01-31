"""NBA Teams Model"""
from datetime import datetime
from typing import Optional, List, Union, Literal, Union
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from backend.common.log import log
from backend.models.base_models import Base
from backend.models.nba.players_model import NBAPlayer



class NBATeam(Base, table=True):
    """NBA Team Model to house the information from the NBA API endpoint CommonTeamYears. Teams are uniquely identified by their team_id, which is a UUID in the NBA API. This model inherits from the NBATeamBase model, which substitutes a UUID for the NBA Team ID from the NBA API."""

        
    id: int = Field(default=None, nullable=False, primary_key=True)

    abbreviation: str = Field(default=None, nullable=False)
    nickname: str = Field(default=None, nullable=False)
    year_founded: int = Field(default=None, nullable=False)
    city: str = Field(default=None, nullable=False)
    arena: str = Field(default=None, nullable=False)
    arena_capacity: int = Field(default=None, nullable=False)
    owner: str = Field(default=None, nullable=False)
    general_manager: str = Field(default=None, nullable=False)
    head_coach: str = Field(default=None, nullable=False)
    dleague_affiliation: str = Field(default=None, nullable=False)
    conference: str = Field(default=None, nullable=False)
    division: str = Field(default=None, nullable=False)
    is_active: bool = Field(default=None, nullable=False)

    players: List["NBAPlayer"] = Relationship(back_populates="team")
    


    def __repr__(self) -> str:
        return f"<NBATeam {self.id}>"