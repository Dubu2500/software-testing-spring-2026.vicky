# language: en
Feature: University flows with multiple actions
  As a student
  I want to perform several actions on university sites
  So that I can verify different types of interactions

  Background:
    Given I am on the Google homepage

  # FLOW 1: Buscar "becas" en el sitio universitario
  @flow1
  Scenario Outline: Search for "becas" on university site and verify results
    When I search for "<search_term>" on Google
    And I click on the first search result
    Then I should be on the domain "<expected_domain>"

    # Usa el término de búsqueda interna que viene de la tabla
    When I search for "<internal_search>" on the university site
    Then I should see results related to "<expected_content>"

    Examples:
      | university | search_term | expected_domain | internal_search | expected_content                          |
      | ITESO      | iteso       | iteso.mx        | becas           | a.gs-title[data-ctorig*='becas.iteso.mx'] |
      | UDG        | udg         | udg.mx          | becas           | a.gs-title[data-ctorig*='cei.udg.mx']     |
      | UNAM       | unam        | unam.mx         | becas           | a.gs-title[data-ctorig*='becas.unam.mx']  |

  # FLOW 2: Hacer clic en un elemento que abre nueva pestaña
  @flow2
  Scenario Outline: Click on element that opens a new tab
    When I search for "<search_term>" on Google
    And I click on the first search result
    Then I should be on the domain "<expected_domain>"

    When I click on the link "<link_selector>" that opens a new tab
    Then I should see on the new tab the title containing "<expected_title>"

    Examples:
      | university | search_term | expected_domain | link_selector                     | expected_title          |
      | ITESO      | iteso       | iteso.mx        | #click_home_radio                 | Radio ITESO             |
      | UDG        | udg         | udg.mx          | a:has-text('Más información')     | Gaceta UDG              |
      | UNAM       | unam        | unam.mx         | a:has(img[alt='Gaceta UNAM'])     | Gaceta UNAM             |

  # FLOW 3: Abrir menu desplegable y seleccionar opcion
  @flow3
  Scenario Outline: Open dropdown menu and select an option
    When I search for "<search_term>" on Google
    And I click on the first search result
    Then I should be on the domain "<expected_domain>"

    When I open the dropdown menu "<menu_selector>" and select "<option_selector>"
    Then I should see the element "<result_selector>" visible

    Examples:
      | university | search_term | expected_domain | menu_selector                          | option_selector                 | result_selector                                               |
      | ITESO      | iteso       | iteso.mx        | button[aria-label='Toggle navigation'] | a:has-text('ACADEMIC PROGRAMS') | span[data-lfr-editable-id='titulo-es-id']                     |
      | UDG        | udg         | udg.mx          | a:has-text('Nuestra Universidad')      | a:has-text('Presentación')      | span:has-text('Presentación')                                 |
      | UNAM       | unam        | unam.mx         | a:has-text('Deportes')                 | a:has-text('Presentación')      | h3:has-text('La Dirección General del Deporte Universitario') |
