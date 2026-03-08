# 🏦 Bank Account System (Python)

A simple **Bank Account System** built with Python using **Object-Oriented Programming (OOP)** concepts.
This project simulates basic banking operations such as **deposit, withdraw, and balance checking with PIN security**.

## 🚀 Features

* Create a bank account with name, balance, and PIN
* Secure PIN verification
* Deposit money
* Withdraw money with rules
* Check account balance
* Private methods and attributes for security

## 🧠 Concepts Used

This project demonstrates the use of:

* Python Classes
* Object-Oriented Programming (OOP)
* Encapsulation
* Private attributes (`__pin`)
* Private methods (`__check_pin`)
* Conditional logic

## 📂 Project Structure

```python
bank_account.py
```

## 💻 Example Usage

```python
b1 = BankAccount("Tuhin", 50000, 4625)

b1.deposit(10000)
b1.withdraw(3000, 4625)

b1.check_blance(4625)

b1.withdraw(3232, 4625)
```

## 📜 Withdrawal Rules

* Maximum withdrawal: **20,000 Taka**
* Amount must be a **multiple of 500**
* Withdrawal not allowed if **balance is insufficient**
* PIN must be correct

## 🛠️ Technologies Used

* Python

## 👨‍💻 Author

**Sabbir Khan**

GitHub: https://github.com/sabbirkhan-dev

---

⭐ If you like this project, feel free to give it a star!
