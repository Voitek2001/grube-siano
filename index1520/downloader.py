
from index1520.api.request.routeRequestParam import RouteRequestParam
from pyhscodes import hscodes
from index1520.service.route_service import RouteService
import pprint
import random

DEPARTURE_COUNTRY_IDS = ["CN"]
DESTINATION_COUNTRY_IDS = ["PL"]

def generateAllPossibleParams(level):
    all_hs = [hs.hscode for hs in hscodes.get_by_level(level)]
    for currDepartureCountryId in DEPARTURE_COUNTRY_IDS:
        for currDestinationCountryId in DESTINATION_COUNTRY_IDS:
            for hs in all_hs:
                yield RouteRequestParam(
                    language="en",
                    view="list",
                    section="route",
                    departureCountryId="CN",
                    destinationCountryId="PL",
                    period="202501-202601",
                    previousPeriod="202301-202401",
                    level=level,
                    hs=[hs],
                )



if __name__ == '__main__':
    from time import sleep
    service = RouteService()
    for currParam in generateAllPossibleParams("2"):

        response = service.getRoute(currParam)
        pprint.pprint(response.model_dump())
        sleep(1 + random.random() + random.randint(1, 2))
        # TODO save reponse to DB


