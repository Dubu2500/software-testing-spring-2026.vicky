# Appium – University Search Tests

Pruebas BDD + DDT para búsqueda de universidades en Google usando **Appium 2**, **WebdriverIO** y **Cucumber**.

---

## Estructura del proyecto

```
appium/
├── features/
│   └── university_search.feature   # Escenarios BDD con tabla de datos (DDT)
├── steps/
│   └── university_search_steps.js  # Step definitions
├── support/
│   └── world.js                    # Contexto global de Cucumber
├── reports/                        # Se genera automáticamente al correr las pruebas
├── cucumber.js                     # Configuración de Cucumber
└── package.json
```

---

## Universidades cubiertas

| Universidad | URL           | Términos buscados          |
|-------------|---------------|----------------------------|
| ITESO       | iteso.mx      | carreras, admisiones       |
| UNE         | une.edu.mx    | carreras, posgrados        |
| CUCEI UDG   | cucei.udg.mx  | carreras, licenciaturas    |

---

## Prerequisitos

### 1. Java JDK 11+
```bash
java -version
```

### 2. Android SDK / Emulador
- Instala Android Studio, o activar opciones de desarrollador con depuracion por usb
- Crea un AVD (dispositivo virtual) con Android 10+
- Inicia el emulador antes de correr las pruebas

### 3. Appium 2 global
```bash
npm install -g appium
appium driver install uiautomator2
```

### 4. Variables de entorno
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk   # Mac
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

Verifica que el emulador esté corriendo:
```bash
adb devices
# Debe mostrar: emulator-5554   device
```

---

## Instalación

```bash
cd google_search_Pextras/appium
npm install
```

---

## Ejecución

### Iniciar Appium server (terminal separada)
```bash
appium
# Appium escucha en http://localhost:4723
```

### Correr todas las pruebas
```bash
npm test
```

### Correr y abrir reporte HTML
```bash
npm run test:report
```

---

## Cómo agregar más universidades (DDT)

Edita la tabla `Examples` en `features/university_search.feature`:

```gherkin
Examples:
  | university | university_url  | search_term   |
  | ITESO      | iteso.mx        | carreras      |
  | UNE        | une.edu.mx      | carreras      |
  | CUCEI UDG  | cucei.udg.mx    | carreras      |
  | TEC        | tec.mx          | carreras      |   <-- nueva fila
```

No necesitas tocar ningún otro archivo. El mismo escenario se ejecuta una vez por cada fila.

---

## Relación con los demás frameworks del equipo

| Framework  | Archivos feature              | Steps                          |
|------------|-------------------------------|--------------------------------|
| Cypress    | `cypress/e2e/*.feature`       | `cypress/support/step_definitions/` |
| Playwright | `playwright/features/*.feature` | `playwright/steps/`           |
| **Appium** | `appium/features/*.feature`   | `appium/steps/`               |

Los tres siguen el mismo patrón BDD con Cucumber y los mismos escenarios, adaptados a su driver correspondiente.
