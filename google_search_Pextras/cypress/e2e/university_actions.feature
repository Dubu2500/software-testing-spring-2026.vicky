Feature: University Website Actions
  As a prospective student
  I want to interact with Mexican university websites
  So that I can find scholarships and navigate their content

  Scenario Outline: Search for becas, verify external links, and follow navigation
    Given I visit the "<university_name>" website at "<home_url>"
    When I search for "becas" at "<search_url>"
    Then the results page should contain "becas"
    And the page should have at least one link that opens in a new tab
    When I click the first visible navigation link
    Then I should be redirected to a different page

  Examples:
    | university_name | home_url                | search_url                                |
    | IPN             | https://www.ipn.mx      | https://www.ipn.mx/becas/                 |
    | UDG             | https://www.udg.mx      | https://www.udg.mx/?s=becas               |
    | ITESO           | https://www.iteso.mx    | https://www.iteso.mx/?s=becas             |
