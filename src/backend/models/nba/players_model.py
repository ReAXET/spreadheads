"""NBA Players Model"""
from typing import Optional
from sqlmodel import Field, Relationship

from backend.models.base_models import Base
from backend.models.nba.teams_model import NBATeam




class NBAPlayer(Base, table=True):
    """NBA Player model object to house the information from the NBA API endpoint CommonAllPlayers. Players are uniquely identified by their player_id, which is a UUID in the NBA API. This model inherits from the NBAPlayerBase model, which substitutes a UUID for the NBA Player ID from the NBA API."""

    id: int = Field(default=None, nullable=False, primary_key=True)
    first_name: str = Field(default=None, nullable=False)
    last_name: str = Field(default=None, nullable=False)
    display_first_last: str = Field(default=None)
    display_last_comma_first: str = Field(default=None)
    display_fi_last: str = Field(default=None)
    team_city: str = Field(default=None)
    team_name: str = Field(default=None, nullable=False)
    team_abbreviation: str = Field(default=None, nullable=False)
    team_conference: str = Field(default=None)
    team_division: str = Field(default=None)
    person_id: int = Field(default=None, nullable=False)
    jersey_number: str = Field(default=None)
    position: str = Field(default=None)
    height: str = Field(default=None)
    weight: str = Field(default=None)
    date_of_birth: str = Field(default=None)
    age: int = Field(default=None)
    affiliation: str = Field(default=None)
    start_year: str = Field(default=None)
    end_year: str = Field(default=None)
    draft_year: str = Field(default=None)
    draft_round: str = Field(default=None)
    draft_number: str = Field(default=None)
    country: str = Field(default=None)
    is_active: bool = Field(default=None, nullable=False)

    team_id: int = Field(default=None, nullable=False, foreign_key="nbateam.id")
    team: Optional[NBATeam] = Relationship(back_populates="nbaplayers")


    class Config:
        table_name = "nba_players"
        from_attributes = True

    def __repr__(self) -> str:
        return f"<NBAPlayer {self.id}>"
    


    