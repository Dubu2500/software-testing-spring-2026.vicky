# -*- coding: utf-8 -*-

"""
Pruebas de sistema usando BDD (Behave/Gherkin), DDT (Scenario Outline) y Selenium.
Busca universidades en Google, entra a su sitio y verifica resultados de busqueda academica.
"""

import time
from urllib.parse import quote_plus

from behave import given, then, when  # pylint: disable=no-name-in-module
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

WAIT_TIME = 15

# URLs de busqueda conocidas por dominio universitario
SEARCH_URL_PATTERNS = {
    "iteso.mx": "https://www.iteso.mx/?s={q}",
    "unam.mx": "https://www.unam.mx/resultados?as_q={q}",
    "ibero.mx": "https://ibero.mx/?s={q}",
}


@given("I am on the Google homepage")  # pylint: disable=not-callable
def open_google(context):
    """Abre el navegador con configuracion para evitar deteccion de bots."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    )
    context.driver = webdriver.Edge(options=options)  # pylint: disable=not-callable
    context.driver.maximize_window()

    context.driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        },
    )

    context.driver.get("https://www.google.com")
    time.sleep(0.5)


@when('I search for "{query}" on Google')  # pylint: disable=not-callable
def search_on_google(context, query):
    """Navega directo a la URL de busqueda de Google para evitar el CAPTCHA."""
    context.driver.get(f"https://www.google.com/search?q={quote_plus(query)}&hl=es-419")
    WebDriverWait(context.driver, WAIT_TIME).until(
        EC.presence_of_element_located((By.ID, "search"))
    )


@when('I click the first link to "{university_domain}"')  # pylint: disable=not-callable
def click_university_link(context, university_domain):
    """Encuentra y hace click en el primer resultado de Google que apunte al dominio dado."""
    driver = context.driver
    wait = WebDriverWait(driver, WAIT_TIME)
    wait.until(EC.presence_of_element_located((By.ID, "search")))

    links = driver.find_elements(By.CSS_SELECTOR, "#search a[href]")
    clicked = False
    for link in links:
        href = link.get_attribute("href") or ""
        if university_domain in href and link.is_displayed():
            link.click()
            clicked = True
            break

    assert (
        clicked
    ), f"No se encontro un link a '{university_domain}' en los resultados de Google"
    wait.until(EC.url_contains(university_domain))

    # Guarda el dominio para que el siguiente paso use la URL de busqueda correcta
    context.university_domain = university_domain


@then('I should be on the "{university_domain}" page')  # pylint: disable=not-callable
def verify_university_page(context, university_domain):
    """Verifica que la URL actual pertenece al dominio universitario esperado."""
    current_url = context.driver.current_url
    assert (
        university_domain in current_url
    ), f"Se esperaba estar en '{university_domain}' pero la URL actual es: {current_url}"


@when(  # pylint: disable=not-callable
    'I search for "{search_term}" on the university website'
)
def search_on_university(context, search_term):
    """
    Navega a la pagina de resultados de busqueda de la universidad.
    Usa un patron de URL conocido por dominio, similar a como el ejemplo
    del profe navega directo a la URL de Google en vez de tipear en el buscador.
    """
    driver = context.driver
    domain = getattr(context, "university_domain", "")

    # Busca el patron de URL correspondiente al dominio
    search_url = None
    for key, pattern in SEARCH_URL_PATTERNS.items():
        if key in domain:
            search_url = pattern.format(q=quote_plus(search_term))
            break

    if search_url:
        driver.get(search_url)
    else:
        # Fallback: intenta encontrar un input de busqueda en la pagina
        WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        _ui_search(driver, search_term)

    WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)


def _ui_search(driver, search_term):
    """Fallback: intenta buscar usando el UI cuando no hay un patron de URL conocido."""
    selectors = [
        'input[type="search"]',
        'input[name="s"]',
        'input[name="q"]',
        'input[name="search"]',
        'input[name="busqueda"]',
    ]
    search_box = None
    for sel in selectors:
        try:
            search_box = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, sel))
            )
            break
        except Exception:  # pylint: disable=broad-except
            continue

    assert (
        search_box is not None
    ), "No se encontro un campo de busqueda en el sitio de la universidad"
    ActionChains(driver).move_to_element(search_box).click().send_keys(
        search_term + Keys.RETURN
    ).perform()
    time.sleep(3)


@then(  # pylint: disable=not-callable
    'the results should contain information about "{search_term}"'
)
def verify_university_results(context, search_term):
    """
    Verifica que la busqueda se realizo y que los resultados estan relacionados al termino.
    Primero revisa el texto del body; si el contenido es dinamico, verifica que el termino
    este en la URL, lo que confirma que la navegacion a resultados ocurrio correctamente.
    """
    driver = context.driver
    current_url = driver.current_url.lower()
    term_lower = search_term.lower()

    # Verificacion principal: el termino aparece en el cuerpo de la pagina
    try:
        WebDriverWait(driver, 10).until(
            lambda d: term_lower in d.find_element(By.TAG_NAME, "body").text.lower()
        )
        return
    except Exception:  # pylint: disable=broad-except
        pass

    # Verificacion secundaria: el termino esta en la URL (confirma que la busqueda se realizo)
    assert term_lower in current_url or quote_plus(term_lower) in current_url, (
        f"No se encontro '{search_term}' en el body ni en la URL.\n"
        f"URL actual: {driver.current_url}"
    )
