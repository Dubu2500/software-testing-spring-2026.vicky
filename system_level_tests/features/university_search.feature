Feature: University Website Search
  As a prospective student
  I want to find a university via Google and search for academic programs on their website
  So that I can discover available educational opportunities

  Scenario Outline: Search for university programs via Google
    Given I am on the Google homepage
    When I search for "<university_name>" on Google
    And I click the first link to "<university_domain>"
    Then I should be on the "<university_domain>" page
    When I search for "<search_term>" on the university website
    Then the results should contain information about "<search_term>"

  Examples:
    | university_name             | university_domain | search_term   |
    | iteso                       | iteso.mx          | carreras      |
    | iteso                       | iteso.mx          | maestrias     |
    | unam                        | unam.mx           | posgrado      |
    | universidad iberoamericana  | ibero.mx          | licenciaturas |
