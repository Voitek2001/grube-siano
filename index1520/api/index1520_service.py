
import requests
from index1520.model.request.routeRequestParam import RouteRequestParam
from index1520.model.response.routeResponse import RouteResponse
API_EXAMPLE = "https://index1520.com/StatisticsAPI/clickhouse/route/?language=en&view=list&section=route&departureCountryId=CN&destinationCountryId=PL&period=202501-202601&previousPeriod=202301-202401&level=2&HS%5B%5D=95&HS%5B%5D=04&HS%5B%5D=96"
import json


class Index1520Service:

    API_BASE = "https://index1520.com/StatisticsAPI/clickhouse/route/"

    def callRoute(self, api_params):
        payload = api_params.model_dump(by_alias=True)
        response = requests.get(
            Index1520Service.API_BASE,
            params=payload
        )

        return RouteResponse(**json.loads(response.content))


if __name__ == '__main__':
    index_service = Index1520Service()
    params = RouteRequestParam(
        language="en",
        view="list",
        section="route",
        departureCountryId="CN",
        destinationCountryId="PL",
        period="202501-202601",
        previousPeriod="202301-202401",
        level=2,
        hs=["95", "04", "96"],
    )
    index_service.callRoute(params)