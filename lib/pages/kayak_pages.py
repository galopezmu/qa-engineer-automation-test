import logging

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_wait_results
from lib.pages.homepage import HomePage
from lib.pages.webelements.kayak_pages_webelements import (
    BestMomentTravelWebElements,
    BusinessWebElements,
    CarsWebElements,
    CytiBreaksWebElements,
    DirectWebElements,
    ExploreWebElements,
    NewsWebElements,
    StaysWebElements,
    TripsWebElements,
)

logger = logging.getLogger(__name__)


class StaysPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = StaysWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.site_dropdown_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.dates_dropdown_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.room_dropdown_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.search_button
            ),
        )


class CarsPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = CarsWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.site_dropdown_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.dates_dropdown_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.search_button
            ),
        )


class CytiBreaksPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = CytiBreaksWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.container_input
            )
        )


class ExplorePage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = ExploreWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.map_container
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.destinations_container
            ),
        )


class NewsPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = NewsWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.header_container
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.content_container
            ),
        )


class DirectPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = DirectWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.container_input
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.routes_container
            ),
        )


class BestMomentTravelPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = BestMomentTravelWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.sites_container
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.date_container
            ),
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.search_button
            ),
        )


class BusinessPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = BusinessWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.search_container
            )
        )


class TripsPage(HomePage):
    def __init__(self, context):
        super().__init__(context)
        self.webElements = TripsWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(
                self.context, self.webElements.header_container
            )
        )
