from pydantic import BaseModel

from index1520.model.response.data import Data
from index1520.model.response.aggregate import Aggregate
from index1520.model.response.meta.meta import Meta
from typing import List
import json


class RouteResponse(BaseModel):
    meta: Meta
    data: List[Data]
    aggregate: Aggregate
    route: str | None
    interval: str | None
    errors: list[str] | None

if __name__ == '__main__':
    with open('example.json') as f:
        a = json.loads(f.read())

    response = RouteResponse(**a)
