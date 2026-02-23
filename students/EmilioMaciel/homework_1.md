# Homework 1: Black Box Testing

## Equivalence Partitioning

### 1. Function that validates credit card numbers.

- Valid card numbers: Length between 13 and 16 digits, containing only numeric digits.

| Input             | Rule                                | Output |
| :---------------- | :---------------------------------- | :----- |
| 1234567890123     | Válida (Longitud 13 y solo números) | True   |
| 1234567890123456  | Válida (Longitud 16 y solo números) | True   |
| 123456789011      | Inválida (Longitud < 13)            | False  |
| 12345678901234567 | Inválida (Longitud > 16)            | False  |
| 123456789012A     | Inválida                            | False  |

### 2. Function that validates dates.

- Valid years: Between 1900 and 2100.
- Valid months: Between 1 and 12.
- Valid days: Between 1 and 31.

| Year | Month | Day | Rule                      | Output |
| :--- | :---- | :-- | :------------------------ | :----- |
| 2000 | 6     | 15  | Todos válidos             | True   |
| 1899 | 1     | 1   | Año fuera de rango (bajo) | False  |
| 2101 | 1     | 1   | Año fuera de rango (alto) | False  |
| 2024 | 0     | 1   | Mes fuera de rango (bajo) | False  |
| 2024 | 13    | 1   | Mes fuera de rango (alto) | False  |
| 2024 | 1     | 0   | Día fuera de rango (bajo) | False  |
| 2024 | 1     | 32  | Día fuera de rango (alto) | False  |

### 3. Function that checks the eligibility of a passenger to book a flight.

- Eligible ages: Between 18 and 65.
- Frequent flyers: True or False.

| Edad | Viajero Frecuente | Clase de Equivalencia                | Resultado Esperado |
| :--- | :---------------- | :----------------------------------- | :----------------- |
| 25   | True              | Edad válida, es viajero frecuente    | Elegible           |
| 40   | False             | Edad válida, no es viajero frecuente | Elegible           |
| 17   | True              | Edad menor al límite                 | No elegible        |
| 66   | False             | Edad mayor al límite                 | No elegible        |

### 4. Function that validates URLs.

- Valid URLs: Length less than or equal to 255, starting with "http://" or "https://".

| URL                  | Clase de Equivalencia           | Resultado Esperado |
| :------------------- | :------------------------------ | :----------------- |
| https://iteso.mx     | Válida (https:// y < 255)       | True               |
| http://google.com    | Válida (http:// y < 255)        | True               |
| hola://hola.com      | Inválida (Protocolo incorrecto) | False              |
| (URL de > 255 chars) | Inválida (Longitud excedida)    | False              |

---

## Boundary Value Analysis

### 1. Function that calculates the eligibility of a person for a loan based on their income and credit score.

- If the income is less than $30,000, the person is not eligible for a loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is above 700, the person is eligible for a standard loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is below or equal to 700, the person is eligible for a secured loan.
- If the income is greater than $60,000 and the credit score is above 750, the person is eligible for a premium loan.
- If the income is greater than $60,000 and the credit score is between 700 and 750 (inclusive), the person is eligible for a standard loan.

| Ingreso | Score | Resultado Esperado | Justificación                              |
| :------ | :---- | :----------------- | :----------------------------------------- |
| $29,999 | 800   | Not Eligible       | Justo debajo del límite de $30k            |
| $30,000 | 701   | Standard           | Límite inferior ingreso, score > 700       |
| $45,000 | 700   | Secured            | Score en el límite de "Secured"            |
| $60,000 | 751   | Standard           | Límite superior 60k, score > 750 (Regla 5) |
| $60,001 | 751   | Premium            | Sobre 60k, score > 750                     |
| $65,000 | 750   | Standard           | Sobre 60k, score en el límite de 750       |

### 2. Function that determines the category of a product in an e-commerce system based on its price.

- Category A: Products priced between $10 and $50 (inclusive).
- Category B: Products priced between $51 and $100 (inclusive).
- Category C: Products priced between $101 and $200 (inclusive).
- Category D: Products priced above $200.

| Precio  | Resultado     | Justificación     |
| :------ | :------------ | :---------------- |
| $9.99   | Sin Categoría | Debajo del mínimo |
| $10.00  | Category A    | Límite inferior A |
| $50.00  | Category A    | Límite superior A |
| $51.00  | Category B    | Límite inferior B |
| $100.00 | Category B    | Límite superior B |
| $101.00 | Category C    | Límite inferior C |
| $200.00 | Category C    | Límite superior C |
| $200.01 | Category D    | Límite inferior D |

### 3. Function that calculates the cost of shipping for packages based on their weight and dimensions.

- Si el peso <= 1 kg y dimensiones <= 10 cm, costo $5.
- Si peso entre 1 y 5 kg y dimensiones entre 11 y 30 cm, costo $10.
- Si peso > 5 kg o dimensiones > 30 cm, costo $20.

| Peso (kg) | Dim (cm) | Resultado | Justificación                      |
| :-------- | :------- | :-------- | :--------------------------------- |
| 1.0       | 10x10x10 | $5        | Límites máximos para costo bajo    |
| 1.1       | 10x10x10 | $10       | Peso apenas excede categoría de $5 |
| 1.0       | 11x10x10 | $10       | Una dimensión apenas excede $5     |
| 5.0       | 30x30x30 | $10       | Límites máximos para costo medio   |
| 5.1       | 30x30x30 | $20       | Peso excede categoría de $10       |
| 3.0       | 31x20x20 | $20       | Dimensión excede categoría de $10  |

---

## Decision Table

1. Create the decision table for a system that provides weather advisories based on temperature and humidity.
   The rules are:
   - Regla 1: Weather recommendation "High temperature and humidity. Stay hydrated." for temperature > 30 and humidity > 70.
   - Regla 2: Weather recommendation "Low temperature. Don't forget your jacket!" for temperature < 0 and any humidity.
   - Regla 3: No weather recommendation for any other temperature and humidity combination.

### 1. Weather Advisories

| Condición                        | Regla 1 | Regla 2 | Regla 3 |
| :------------------------------- | :-----: | :-----: | :-----: |
| Temperatura > 30                 |   SÍ    |   NO    |   NO    |
| Humedad > 70                     |   SÍ    |    -    |   NO    |
| Temperatura < 0                  |   NO    |   SÍ    |   NO    |
| **Acción**                       |         |         |         |
| "High temp/hum. Stay hydrated"   |    X    |         |         |
| "Low temp. Don't forget jacket!" |         |    X    |         |
| No recommendation                |         |         |    X    |

2. Create the decision table for a system that authenticates users based on their username and password.
   The rules are:
   - Returns "Admin" for username "admin" and password "admin123".
   - Returns "User" for any other username with at least 5 characters and password with at least 8 characters.
   - Returns "Invalid" if the username or password lenghts are not met.

### 2. User Authentication

| Condición              | R1  | R2  | R3  |
| :--------------------- | :-: | :-: | :-: |
| Username es "admin"    | SÍ  | NO  | NO  |
| Password es "admin123" | SÍ  | SÍ  | NO  |
| Username longitud >= 5 | SÍ  | SÍ  | SÍ  |
| Password longitud >= 8 | SÍ  | SÍ  | SÍ  |
| **Resultado**          |     |     |     |
| "Admin"                |  X  |     |     |
| "User"                 |     |  X  |  X  |
| "Invalid"              |     |     |     |
