# Homework 1 - Black Box Testing (Equivalence Partitioning, BVA, Decision Table)

## Equivalence Partitioning

## 1. Function that validates credit card numbers.

**Rules:**

- Valid card numbers: length between 13 and 16 digits (inclusive).
- Must contain only numeric digits.

### Test Cases

| Test Case | Input               | Expected Output | Description                                  |
| --------- | ------------------- | --------------- | -------------------------------------------- |
| TC1.1     | `1234567890123`     | Valid           | Valid partition: 13 digits, numeric only     |
| TC1.2     | `1234567890123456`  | Valid           | Valid partition: 16 digits, numeric only     |
| TC1.3     | `123456789012`      | Invalid         | Invalid partition: length below 13           |
| TC1.4     | `12345678901234567` | Invalid         | Invalid partition: length above 16           |
| TC1.5     | `12345abc90123`     | Invalid         | Invalid partition: contains alphabetic chars |
| TC1.6     | `1234-5678-9012`    | Invalid         | Invalid partition: contains special chars    |
| TC1.7     | `` (empty)          | Invalid         | Invalid partition: empty input               |

## 2. Function that validates dates.

**Rules:**

- Valid year: 1900 to 2100.
- Valid month: 1 to 12.
- Valid day: 1 to 31.

### Test Cases

| Test Case | Input (YYYY, MM, DD) | Expected Output | Description                                |
| --------- | -------------------- | --------------- | ------------------------------------------ |
| TC2.1     | (2000, 6, 15)        | Valid           | Valid partition for year, month, and day   |
| TC2.2     | (1900, 1, 1)         | Valid           | Valid boundary values for all fields       |
| TC2.3     | (2100, 12, 31)       | Valid           | Valid upper boundary values for all fields |
| TC2.4     | (1899, 6, 15)        | Invalid         | Invalid partition: year below minimum      |
| TC2.5     | (2101, 6, 15)        | Invalid         | Invalid partition: year above maximum      |
| TC2.6     | (2000, 0, 15)        | Invalid         | Invalid partition: month below minimum     |
| TC2.7     | (2000, 13, 15)       | Invalid         | Invalid partition: month above maximum     |
| TC2.8     | (2000, 6, 0)         | Invalid         | Invalid partition: day below minimum       |
| TC2.9     | (2000, 6, 32)        | Invalid         | Invalid partition: day above maximum       |

## 3. Function that checks passenger eligibility to book a flight.

**Rules:**

- Eligible age: 18 to 65 (inclusive).
- Frequent flyer value: `True` or `False`.

### Test Cases

| Test Case | Input (Age, Frequent Flyer) | Expected Output | Description                                         |
| --------- | --------------------------- | --------------- | --------------------------------------------------- |
| TC3.1     | (25, True)                  | Eligible        | Valid partition: age in range, frequent flyer true  |
| TC3.2     | (25, False)                 | Eligible        | Valid partition: age in range, frequent flyer false |
| TC3.3     | (18, True)                  | Eligible        | Boundary: minimum eligible age                      |
| TC3.4     | (65, False)                 | Eligible        | Boundary: maximum eligible age                      |
| TC3.5     | (17, True)                  | Not Eligible    | Invalid partition: age below minimum                |
| TC3.6     | (66, False)                 | Not Eligible    | Invalid partition: age above maximum                |
| TC3.7     | (30, `yes`)                 | Invalid Input   | Invalid partition: frequent flyer not boolean       |

## 4. Function that validates URLs.

**Rules:**

- Length must be less than or equal to 255 characters.
- Must start with `http://` or `https://`.

### Test Cases

| Test Case | Input                      | Expected Output | Description                                       |
| --------- | -------------------------- | --------------- | ------------------------------------------------- |
| TC4.1     | `http://example.com`       | Valid           | Valid partition: proper protocol and short length |
| TC4.2     | `https://example.com/path` | Valid           | Valid partition: secure protocol and valid length |
| TC4.3     | `ftp://example.com`        | Invalid         | Invalid partition: unsupported protocol           |
| TC4.4     | `www.example.com`          | Invalid         | Invalid partition: missing required protocol      |
| TC4.5     | `http://` + 248 chars      | Valid           | Boundary: exactly 255 total characters            |
| TC4.6     | `http://` + 249 chars      | Invalid         | Boundary: 256 total characters                    |
| TC4.7     | `` (empty)                 | Invalid         | Invalid partition: empty input                    |

## Boundary Value Analysis

## 5. Function that calculates loan eligibility (income, credit score).

**Rules:**

- Income < 30000: Not eligible.
- 30000 to 60000 (inclusive) and credit score > 700: Standard loan.
- 30000 to 60000 (inclusive) and credit score <= 700: Secured loan.
- Income > 60000 and credit score > 750: Premium loan.
- Income > 60000 and credit score 700 to 750 (inclusive): Standard loan.

### Test Cases

| Test Case | Input (Income, Credit Score) | Expected Output | Description                                             |
| --------- | ---------------------------- | --------------- | ------------------------------------------------------- |
| TC5.1     | (29999, 720)                 | Not Eligible    | Boundary: income just below 30000                       |
| TC5.2     | (30000, 700)                 | Secured Loan    | Boundary: income at 30000, score at 700                 |
| TC5.3     | (30000, 701)                 | Standard Loan   | Boundary: score just above 700 in middle income tier    |
| TC5.4     | (60000, 700)                 | Secured Loan    | Boundary: upper income limit, score at 700              |
| TC5.5     | (60000, 701)                 | Standard Loan   | Boundary: upper income limit, score just above 700      |
| TC5.6     | (60001, 700)                 | Standard Loan   | Boundary: income just above 60000 with score in 700-750 |
| TC5.7     | (60001, 750)                 | Standard Loan   | Boundary: upper standard score for high income          |
| TC5.8     | (60001, 751)                 | Premium Loan    | Boundary: score just above 750 for high income          |
| TC5.9     | (70000, 680)                 | Not Eligible    | Out-of-rule partition: income > 60000 but score < 700   |

## 6. Function that determines product category based on price.

**Rules:**

- Category A: 10 to 50 (inclusive).
- Category B: 51 to 100 (inclusive).
- Category C: 101 to 200 (inclusive).
- Category D: greater than 200.

### Test Cases

| Test Case | Input (Price) | Expected Output | Description                             |
| --------- | ------------- | --------------- | --------------------------------------- |
| TC6.1     | 9             | Invalid         | Boundary: just below Category A minimum |
| TC6.2     | 10            | Category A      | Boundary: Category A minimum            |
| TC6.3     | 50            | Category A      | Boundary: Category A maximum            |
| TC6.4     | 51            | Category B      | Boundary: Category B minimum            |
| TC6.5     | 100           | Category B      | Boundary: Category B maximum            |
| TC6.6     | 101           | Category C      | Boundary: Category C minimum            |
| TC6.7     | 200           | Category C      | Boundary: Category C maximum            |
| TC6.8     | 201           | Category D      | Boundary: Category D minimum (>200)     |

## 7. Function that calculates shipping cost by weight and dimensions.

**Rules:**

- Cost = $5 when weight <= 1 kg and length, width, height are each <= 10 cm.
- Cost = $10 when weight is 1 to 5 kg (inclusive) and each dimension is 11 to 30 cm (inclusive).
- Cost = $20 when weight > 5 kg or any dimension > 30 cm.

### Test Cases

| Test Case | Input (Weight, L, W, H) | Expected Output | Description                                          |
| --------- | ----------------------- | --------------- | ---------------------------------------------------- |
| TC7.1     | (1.0, 10, 10, 10)       | $5              | Boundary: max values for $5 tier                     |
| TC7.2     | (0.99, 9, 10, 8)        | $5              | Typical case within $5 tier                          |
| TC7.3     | (1.0, 11, 11, 11)       | $10             | Boundary: weight at 1 and dimensions at tier minimum |
| TC7.4     | (5.0, 30, 30, 30)       | $10             | Boundary: max values for $10 tier                    |
| TC7.5     | (5.01, 20, 20, 20)      | $20             | Boundary: weight just above 5                        |
| TC7.6     | (3.0, 31, 20, 20)       | $20             | Boundary: one dimension just above 30                |
| TC7.7     | (6.0, 10, 10, 10)       | $20             | Typical case with weight > 5                         |

## Decision Table

## 8. Decision table for weather advisories (temperature, humidity).

### Decision Table

| Conditions / Actions                           | Rule 1 | Rule 2 | Rule 3 |
| ---------------------------------------------- | ------ | ------ | ------ |
| Temperature > 30                               | Y      | N      | N      |
| Humidity > 70                                  | Y      | -      | -      |
| Temperature < 0                                | N      | Y      | N      |
| Action: High temperature and humidity advisory | X      | -      | -      |
| Action: Low temperature jacket advisory        | -      | X      | -      |
| Action: No recommendation                      | -      | -      | X      |

### Test Cases

| Test Case | Input (Temperature, Humidity) | Expected Output                               | Description                               |
| --------- | ----------------------------- | --------------------------------------------- | ----------------------------------------- |
| TC8.1     | (31, 71)                      | High temperature and humidity. Stay hydrated. | Matches Rule 1                            |
| TC8.2     | (-1, 20)                      | Low temperature. Don't forget your jacket!    | Matches Rule 2 with any humidity          |
| TC8.3     | (30, 71)                      | No weather recommendation                     | Boundary: temperature not greater than 30 |
| TC8.4     | (31, 70)                      | No weather recommendation                     | Boundary: humidity not greater than 70    |
| TC8.5     | (15, 50)                      | No weather recommendation                     | Typical non-matching values               |

## 9. Decision table for authentication (username, password).

### Decision Table

| Conditions / Actions     | Rule 1 | Rule 2 | Rule 3 |
| ------------------------ | ------ | ------ | ------ |
| Username = `admin`       | Y      | N      | -      |
| Password = `admin123`    | Y      | N      | -      |
| Username length >= 5     | -      | Y      | N      |
| Password length >= 8     | -      | Y      | N      |
| Action: Return `Admin`   | X      | -      | -      |
| Action: Return `User`    | -      | X      | -      |
| Action: Return `Invalid` | -      | -      | X      |

### Test Cases

| Test Case | Input (Username, Password) | Expected Output | Description                                          |
| --------- | -------------------------- | --------------- | ---------------------------------------------------- |
| TC9.1     | (`admin`, `admin123`)      | Admin           | Exact admin credentials                              |
| TC9.2     | (`maria1`, `passw0rd`)     | User            | Non-admin user with valid lengths                    |
| TC9.3     | (`user`, `passw0rd`)       | Invalid         | Username length below 5                              |
| TC9.4     | (`johndoe`, `pass12`)      | Invalid         | Password length below 8                              |
| TC9.5     | (`admin`, `wrongpass`)     | User            | Admin username but not admin password; valid lengths |
| TC9.6     | (`adm`, `123`)             | Invalid         | Both username and password lengths not met           |
