# Homework 1 - Black Box Testing Exercises 1 to 5

## 1. Function that checks if a given number is positive, negative, or zero.

**Rules:**

- If the number is greater than 0, it is **positive**.
- If the number is less than 0, it is **negative**.
- If the number is equal to 0, it is **zero**.

### Test Cases

| Test Case | Input | Expected Output | Description                         |
| --------- | ----- | --------------- | ----------------------------------- |
| TC1.1     | 5     | Positive        | Typical positive number             |
| TC1.2     | 100   | Positive        | Large positive number               |
| TC1.3     | 0.5   | Positive        | Small positive decimal              |
| TC1.4     | 1     | Positive        | Boundary: smallest positive integer |
| TC1.5     | -5    | Negative        | Typical negative number             |
| TC1.6     | -100  | Negative        | Large negative number               |
| TC1.7     | -0.5  | Negative        | Small negative decimal              |
| TC1.8     | -1    | Negative        | Boundary: largest negative integer  |
| TC1.9     | 0     | Zero            | Boundary: zero                      |

## 2. Function that validates user passwords.

**The password validation rules are as follows:**

- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter.
- The password must contain at least one lowercase letter.
- The password must contain at least one digit.
- The password must contain at least one special character (!, @, #, $, %, or &).

### Test Cases

| Test Case | Input           | Expected Output | Description                                                                |
| --------- | --------------- | --------------- | -------------------------------------------------------------------------- |
| TC2.1     | `Abcdef1!`      | Valid           | Minimum valid password (8 chars, has uppercase, lowercase, digit, special) |
| TC2.2     | `MyPass99@Word` | Valid           | Longer valid password with multiple of each type                           |
| TC2.3     | `Aa1!Bb2@`      | Valid           | Valid password with multiple special characters                            |
| TC2.4     | `Ab1!`          | Invalid         | Too short (4 chars) — fails minimum length                                 |
| TC2.5     | `Abcdef1`       | Invalid         | 7 characters — one below minimum length                                    |
| TC2.6     | `abcdef1!`      | Invalid         | Missing uppercase letter                                                   |
| TC2.7     | `ABCDEF1!`      | Invalid         | Missing lowercase letter                                                   |
| TC2.8     | `Abcdefg!`      | Invalid         | Missing digit                                                              |
| TC2.9     | `Abcdefg1`      | Invalid         | Missing special character                                                  |
| TC2.10    | `abcdefgh`      | Invalid         | Missing uppercase, digit, and special character                            |
| TC2.11    | `ABCDEFGH`      | Invalid         | Missing lowercase, digit, and special character                            |
| TC2.12    | `12345678`      | Invalid         | Missing uppercase, lowercase, and special character                        |
| TC2.13    | `!!!!!!!!`      | Invalid         | Missing uppercase, lowercase, and digit                                    |
| TC2.14    | `` (empty)      | Invalid         | Empty string — fails all rules                                             |
| TC2.15    | `Aa1#Bb2$Cc3%`  | Valid           | Valid password using #, $, % special characters                            |
| TC2.16    | `Hello&World1`  | Valid           | Valid password using & as special character                                |

## 3. Function that calculates the discount for a customer's purchase based on the total amount.

**The discount rules are as follows:**

- If the total amount is less than 100, no discount is applied.
- If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
- If the total amount is greater than 500, a 20% discount is applied.

### Test Cases

| Test Case | Input (Total Amount) | Discount | Expected Output (Final Price) | Description                       |
| --------- | -------------------- | -------- | ----------------------------- | --------------------------------- |
| TC3.1     | $0                   | 0%       | $0                            | Boundary: zero amount             |
| TC3.2     | $50                  | 0%       | $50                           | Typical amount below 100          |
| TC3.3     | $99                  | 0%       | $99                           | Boundary: just below 100          |
| TC3.4     | $99.99               | 0%       | $99.99                        | Boundary: one cent below 100      |
| TC3.5     | $100                 | 10%      | $90                           | Boundary: exactly 100 (inclusive) |
| TC3.6     | $100.01              | 10%      | $90.01                        | Boundary: just above 100          |
| TC3.7     | $300                 | 10%      | $270                          | Typical amount in 100–500 range   |
| TC3.8     | $500                 | 10%      | $450                          | Boundary: exactly 500 (inclusive) |
| TC3.9     | $500.01              | 20%      | $400.01                       | Boundary: just above 500          |
| TC3.10    | $501                 | 20%      | $400.80                       | Boundary: one above 500           |
| TC3.11    | $1000                | 20%      | $800                          | Typical amount above 500          |

## 4. Function that processes user orders in an e-commerce system.

The function calculates the total price of the items in the order, applying different discounts based on the quantity of each item.

**The discount rules are as follows:**

- If the quantity of a single item is between 1 and 5 (inclusive), no discount is applied.
- If the quantity of a single item is between 6 and 10 (inclusive), a 5% discount is applied.
- If the quantity of a single item is greater than 10, a 10% discount is applied.

### Test Cases

| Test Case | Items (Name, Price, Qty)                           | Discount per Item    | Expected Total | Description                                      |
| --------- | -------------------------------------------------- | -------------------- | -------------- | ------------------------------------------------ |
| TC4.1     | Item A: $10 x 1                                    | 0%                   | $10.00         | Boundary: minimum quantity (1), no discount      |
| TC4.2     | Item A: $10 x 3                                    | 0%                   | $30.00         | Typical quantity in 1–5 range                    |
| TC4.3     | Item A: $10 x 5                                    | 0%                   | $50.00         | Boundary: upper limit of no-discount range       |
| TC4.4     | Item A: $10 x 6                                    | 5%                   | $57.00         | Boundary: lower limit of 5% discount range       |
| TC4.5     | Item A: $10 x 8                                    | 5%                   | $76.00         | Typical quantity in 6–10 range                   |
| TC4.6     | Item A: $10 x 10                                   | 5%                   | $95.00         | Boundary: upper limit of 5% discount range       |
| TC4.7     | Item A: $10 x 11                                   | 10%                  | $99.00         | Boundary: lower limit of 10% discount range      |
| TC4.8     | Item A: $10 x 20                                   | 10%                  | $180.00        | Typical quantity above 10                        |
| TC4.9     | Item A: $20 x 3, Item B: $15 x 7                   | A: 0%, B: 5%         | $159.75        | Multiple items with different discount tiers     |
| TC4.10    | Item A: $10 x 5, Item B: $20 x 10, Item C: $5 x 15 | A: 0%, B: 5%, C: 10% | $307.50        | Multiple items spanning all three discount tiers |
| TC4.11    | Item A: $50 x 1                                    | 0%                   | $50.00         | Single expensive item, no discount               |
| TC4.12    | Item A: $100 x 11                                  | 10%                  | $990.00        | Large order with 10% discount                    |

**Calculation details for multi-item test cases:**

- **TC4.9:** Item A = $20 x 3 = $60.00 (0%) + Item B = $15 x 7 = $105 x 0.95 = $99.75 (5%) = **$159.75**
- **TC4.10:** Item A = $10 x 5 = $50.00 (0%) + Item B = $20 x 10 = $200 x 0.95 = $190.00 (5%) + Item C = $5 x 15 = $75 x 0.90 = $67.50 (10%) = **$307.50**

## 5. Function that calculates shipping costs for an online shopping system.

The function calculates shipping costs based on the total weight of the items in the order and the shipping method chosen by the customer.

**The shipping cost rules are as follows:**

**For standard shipping:**

- If the total weight is less than or equal to 5 kg, the cost is $10.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $15.
- If the total weight is greater than 10 kg, the cost is $20.

**For express shipping:**

- If the total weight is less than or equal to 5 kg, the cost is $20.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $30.
- If the total weight is greater than 10 kg, the cost is $40.

### Test Cases

| Test Case | Shipping Method | Total Weight (kg) | Expected Cost | Description                                        |
| --------- | --------------- | ----------------- | ------------- | -------------------------------------------------- |
| TC5.1     | Standard        | 1                 | $10           | Light package, standard shipping                   |
| TC5.2     | Standard        | 3                 | $10           | Typical weight within 0–5 kg range                 |
| TC5.3     | Standard        | 5                 | $10           | Boundary: exactly 5 kg (inclusive in first tier)   |
| TC5.4     | Standard        | 5.01              | $15           | Boundary: just above 5 kg                          |
| TC5.5     | Standard        | 7                 | $15           | Typical weight in 5–10 kg range                    |
| TC5.6     | Standard        | 10                | $15           | Boundary: exactly 10 kg (inclusive in second tier) |
| TC5.7     | Standard        | 10.01             | $20           | Boundary: just above 10 kg                         |
| TC5.8     | Standard        | 15                | $20           | Typical weight above 10 kg                         |
| TC5.9     | Standard        | 50                | $20           | Large weight, standard shipping                    |
| TC5.10    | Express         | 1                 | $20           | Light package, express shipping                    |
| TC5.11    | Express         | 3                 | $20           | Typical weight within 0–5 kg range                 |
| TC5.12    | Express         | 5                 | $20           | Boundary: exactly 5 kg (inclusive in first tier)   |
| TC5.13    | Express         | 5.01              | $30           | Boundary: just above 5 kg                          |
| TC5.14    | Express         | 7                 | $30           | Typical weight in 5–10 kg range                    |
| TC5.15    | Express         | 10                | $30           | Boundary: exactly 10 kg (inclusive in second tier) |
| TC5.16    | Express         | 10.01             | $40           | Boundary: just above 10 kg                         |
| TC5.17    | Express         | 15                | $40           | Typical weight above 10 kg                         |
| TC5.18    | Express         | 50                | $40           | Large weight, express shipping                     |
