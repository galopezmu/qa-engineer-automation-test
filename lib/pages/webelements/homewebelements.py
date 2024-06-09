from selenium.webdriver.common.by import By


class HomeWebElements:
    # Corregimos los locators desactualizados
    search_form = (By.CSS_SELECTOR, "#main-search-form")
    signin_button = (By.CSS_SELECTOR, ".J-sA")

    # Añadimos los nuevos elementos para validar la página principal
    origin_dropdown_input = (By.CSS_SELECTOR, ".zEiP-origin")
    destination_dropdown_input = (By.CSS_SELECTOR, ".zEiP-destination")
    dates_dropdown_input = (By.CSS_SELECTOR, ".zEiP-dates")
    search_button = (By.CSS_SELECTOR, ".zEiP-submit")
