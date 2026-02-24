
from typing import List
from pydantic import BaseModel, Field


class RouteRequestParam(BaseModel):
    language: str
    view: str
    section: str
    departureCountryId: str
    destinationCountryId: str
    period: str
    previousPeriod: str
    level: int
    hs: List[str] = Field(alias="HS[]")

    model_config = {
        "populate_by_name": True
    }