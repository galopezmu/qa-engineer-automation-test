from selenium.webdriver.common.by import By


class StaysWebElements:
    site_dropdown_input = (
        By.CSS_SELECTOR,
        ".TWls.TWls-mod-size-large.TWls-mod-variant-prefix",
    )
    dates_dropdown_input = (By.CSS_SELECTOR, ".cBaN-date-select-wrapper")
    room_dropdown_input = (By.CSS_SELECTOR, ".c3JX7-wrapper")
    search_button = (By.CSS_SELECTOR, ".RxNS-button-container")


class CarsWebElements(StaysWebElements):
    pass


class CytiBreaksWebElements:
    container_input = (By.CSS_SELECTOR, ".EFi3-content")


class ExploreWebElements:
    map_container = (By.CSS_SELECTOR, ".Ui-Explore-Components-MapContainer-container")
    destinations_container = (By.CSS_SELECTOR, ".anywhere-drawer")


class NewsWebElements:
    header_container = (By.CSS_SELECTOR, ".swiper-wrapper")
    content_container = (
        By.CSS_SELECTOR,
        ".wp-block-r9-multi-section.alignwide.r9-multi.section.section--no-padding",
    )


class DirectWebElements:
    container_input = (
        By.CSS_SELECTOR,
        "#main > div.ylgR > div > div.kml-row.mod-row-compact",
    )
    routes_container = (
        By.CSS_SELECTOR,
        "#main > div.ylgR > div > div.ylgR-routes",
    )


class BestMomentTravelWebElements:
    sites_container = (
        By.CSS_SELECTOR,
        "#main > div > div.IMh_ > div.kml-layout.mod-wide.edges-m.mobile-edges.lyx0.c31EJ > div > div > div > div.c7IFH-smarty-container",
    )
    date_container = (
        By.CSS_SELECTOR,
        "#main > div > div.IMh_ > div.kml-layout.mod-wide.edges-m.mobile-edges.lyx0.c31EJ > div > div > div > div:nth-child(2) > div",
    )
    search_button = (
        By.CSS_SELECTOR,
        "#main > div > div.IMh_ > div.kml-layout.mod-wide.edges-m.mobile-edges.lyx0.c31EJ > div > div > div > button",
    )


class BusinessWebElements:
    search_container = (
        By.CSS_SELECTOR,
        "#main > div.l-6h > div > div.J1TT > div > div.GEsl > form > div.GEsl-form-row",
    )


class TripsWebElements:
    header_container = (By.CSS_SELECTOR, ".c7Ucr")
