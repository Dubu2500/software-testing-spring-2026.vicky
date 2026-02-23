# Oscar Clemente López Labrador - 72031

# 1. Function that checks if a given number is positive, negative, or zero.

---

### Equivalence Partitioning (3 Scenarios)

| **Cases** | **Input** | **Expected Output** |
| --------- | --------- | ------------------- |
| Positive  | 10        | Positive            |
| Negative  | -3        | Negative            |
| Zero      | 0         | Zero                |

# 2. Function that validates user passwords.

The password validation rules are as follows:

- The password must be at least 8 characters long.
- The password must contain at least:
  - one uppercase letter,
  - one lowercase letter,
  - one digit, and
  - one special character (!, @, #, $, %, or &).

---

### Equivalence Partitioning

| **Cases**                 | Input           | **Expected Output** |
| ------------------------- | --------------- | ------------------- |
| Valid                     | LisanAlGaib777! | true                |
| Not long enough           | Key123!         | false               |
| Missing uppercase letter  | holamundo123!   | false               |
| Missing lowercase letter  | HOLAMUNDO123!   | false               |
| Missing digit             | HolaMundo!      | false               |
| Missing special character | HolaMundo123    | false               |

# 3. Function that calculates the discount for a customer's purchase based on the total amount.

The discount rules are as follows:

- If the total amount is less than 100, no discount is applied.
- If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
- If the total amount is greater than 500, a 20% discount is applied.

---

### Decision Table

| **Cases**         | **Input** | **Expected Output (Final Price)** |
| ----------------- | --------- | --------------------------------- |
| total < 100       | 44        | 44                                |
| 100 ≤ total ≤ 500 | 250       | 225                               |
| total > 500       | 1000      | 800                               |

# 4. Function that processes user orders in an e-commerce system.

The function calculates the total price of the items in the order, applying different discounts based on the quantity of each item.

The discount rules are as follows:

- If the quantity of a single item is between 1 and 5 (inclusive), no discount is applied.
- If the quantity of a single item is between 6 and 10 (inclusive), a 5% discount is applied.
- If the quantity of a single item is greater than 10, a 10% discount is applied.

---

### Decision Table

| Item Quantity (q) | Discount Applied |
| ----------------- | ---------------- |
| 1 ≤ q ≤ 5         | 0%               |
| 6 ≤ q ≤ 10        | 5%               |
| q > 10            | 10%              |

# 5. Function that calculates shipping costs for an online shopping system.

The function calculates shipping costs based on the total weight of the items in the order and the shipping method chosen by the customer.

The shipping cost rules are as follows:

For standard shipping:

- If the total weight is less than or equal to 5 kg, the cost is $10.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $15.
- If the total weight is greater than 10 kg, the cost is $20.

For express shipping:

- If the total weight is less than or equal to 5 kg, the cost is $20.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $30.
- If the total weight is greater than 10 kg, the cost is $40.

---

### Decision Table

| Shipping Method | Total Weight (kg) | **Expected Output ($)** |
| --------------- | ----------------- | ----------------------- |
| Standard        | ≤ 5               | 10                      |
| Standard        | > 5 and ≤ 10      | 15                      |
| Standard        | > 10              | 20                      |
| Express         | ≤ 5               | 20                      |
| Express         | > 5 and ≤ 10      | 30                      |
| Express         | > 10              | 40                      |
