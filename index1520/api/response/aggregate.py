from pydantic import BaseModel


class Aggregate(BaseModel):
    departureId: int | None
    destinationId: int | None
    currentPeriodTeu: str | None
    currentPeriodActualWeight: float | None
    currentPeriodShippingQty: float | None
    currentPeriodTime: float | None
    currentPeriodTransitTime: float | None
    currentPeriodFullTime: float | None
    previousPeriodTeu: str | None
    previousPeriodActualWeight: float | None
    previousPeriodShippingQty: float | None
    previousPeriodTime: float | None
    previousPeriodTransitTime: float | None
    previousPeriodFullTime: float | None
    relativeTeu: float | None
    relativeActualWeight: float | None
    relativeShippingQty: float | None
    relativeTime: float | None
    relativeTransitTime: float | None
    relativeFullTime: float | None
