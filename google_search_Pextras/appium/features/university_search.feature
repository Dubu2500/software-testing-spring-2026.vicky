Feature: University Search on Google

  As a user
  I want to search for universities on Google
  So that I can navigate to their websites and find information about their programs

  Background:
    Given I open Google in the browser

  Scenario Outline: Search on Google then open official section by URL map (no mailto, no SERP parsing)
    When I search for "<university>" on Google
    And I open the official "<section>" page for "<university>"
    Then the current URL should contain the expected official host
    When I search for "<search_term>" within the page using id-first selectors
    Then I should see results related to "<search_term>"

    Examples:
      | university  | section       | search_term   |
      | ITESO       | carreras      | Ingeniería    |
      | ITESO       | posgrados     | Maestría      |
      | ITESO       | admisiones    | examen        |
      | UNE         | carreras      | licenciatura  |
      | UNE         | posgrados     | posgrados     |
      | UNE         | planteles     | plantel       |
      | UNE         | admisiones    | ingreso       |
      | CUCEI UDG   | licenciaturas | Computación   |
      | CUCEI UDG   | posgrados     | Doctorado     |
      | CUCEI UDG   | home          | Oferta        |
