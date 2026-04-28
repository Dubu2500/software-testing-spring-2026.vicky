"""Hooks de Behave para setup y teardown de cada escenario."""


def after_scenario(context, _scenario):
    """Cierra el navegador al terminar cada escenario."""
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
        context.driver = None
