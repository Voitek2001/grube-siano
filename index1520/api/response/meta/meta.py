
from pydantic import BaseModel

from index1520.api.response.meta.period import Period

class Meta(BaseModel):
    success: bool
    totalTimeRequest: float
    count: int
    period: Period
