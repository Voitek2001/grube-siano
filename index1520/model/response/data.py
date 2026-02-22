from pydantic import BaseModel


class Data(BaseModel):
    departureName: str
    departureId: str
    destinationId: str
    destinationName: str
    currentPeriodTeu: str
    currentPeriodActualWeight: float
    currentPeriodShippingQty: float
    currentPeriodTime: float
    currentPeriodTransitTime: float
    currentPeriodFullTime: float
    previousPeriodTeu: str
    previousPeriodActualWeight: float
    previousPeriodShippingQty: float
    previousPeriodTime: float
    previousPeriodTransitTime: float
    previousPeriodFullTime: float
    relativeTeu: float
    relativeActualWeight: float
    relativeShippingQty: float
    relativeTime: float
    relativeTransitTime: float
    relativeFullTime: float
