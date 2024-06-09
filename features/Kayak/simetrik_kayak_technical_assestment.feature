@simetrik_technical_challenge
Feature: Visit each Kayak menu otion

    Scenario: Navigate to the Kayak home page and validate principal elements
            """
            Validamos que estemos en la página de Kayak
            """

        Given I navigate to the kayak main page
        Then I should be in the "home" page
        And The page "should" contain the next elements
            | name                 | type   |
            | origin_dropdown      | input  |
            | destination_dropdown | input  |
            | dates_dropdown       | input  |
            | search               | button |

    Scenario Outline: Navigate through each option in the left menu of the Kayak page and validate that it opens correctly
            """
            Realizamos la navegación entre cada página del menú de la izquierda
            Verificamos que la URL corresponda a la de cada página
            Verificamos que se muestren los elementos de la página
            """
        Given I navigate to the kayak main page
        Then I should be in the "home" page
        When I navigate to the "<url>" URL
        Then The url page should be equal to the next "<url>" url
        And I should be in the "<page>" page

        Examples:
            | page               | url                                                   |
            | stays              | https://www.kayak.com.co/stays                        |
            | cars               | https://www.kayak.com.co/cars                         |
            | city_breaks        | https://www.kayak.com.co/citybreaks                   |
            | explore            | https://www.kayak.com.co/explore/                     |
            | news               | https://www.kayak.com.co/news/                        |
            | direct             | https://www.kayak.com.co/direct                       |
            | best_moment_travel | https://www.kayak.com.co/el-mejor-momento-para-viajar |
            | business           | https://www.kayak.com.co/business                     |
            | trips              | https://www.kayak.com.co/trips                        |
