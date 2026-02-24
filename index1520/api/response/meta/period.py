
from pydantic import BaseModel, Field


class CompareWith(BaseModel):
    from_: str = Field(alias="from")
    to: str

class ReportingPeriod(BaseModel):
    from_: str = Field(alias="from")
    to: str

class Period(BaseModel):
    reportingPeriod: ReportingPeriod
    compareWith: CompareWith

