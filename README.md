# Clover Shop 🛒

A simple command-line shopping program written in Python.

This project simulates a basic shopping experience where a user can select a product, enter a quantity, optionally purchase another product, and receive a receipt showing the total cost.

## 📌 Project Overview

**Clover Shop** is a beginner Python project created to practice fundamental programming concepts.

The program displays a list of available products and their prices. The user selects a product by entering its number, provides the desired quantity, and can choose whether to purchase another product.

At the end of the transaction, the program generates a simple receipt containing the purchased products and the total amount.

## 🛍️ Available Products

| No. | Product     |   Price |
| --: | ----------- | ------: |
|   1 | Rice        | N50,000 |
|   2 | Chicken     |  N8,000 |
|   3 | Cooking Oil | N12,000 |
|   4 | Sugar       |  N5,000 |
|   5 | Milk        |  N4,000 |

## ⚙️ Features

* Displays available products and prices
* Allows the user to select a product
* Accepts product quantities
* Calculates the cost based on quantity
* Allows the user to purchase a second product
* Calculates the total cost
* Generates a simple receipt
* Handles some invalid responses with a command error message
* Uses Nigerian Naira (`N`) for prices

## 🧠 Python Concepts Practiced

This project was built to practice several fundamental Python concepts:

* `print()` statements
* Variables
* Lists
* `for` loops
* `input()`
* Type conversion using `int()`
* Functions
* `if`, `elif`, and `else` statements
* Nested conditional statements
* Arithmetic operations
* F-strings
* Basic program flow and user interaction

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Enter the project directory

```bash
cd YOUR-REPOSITORY
```

### 3. Run the program

```bash
python3 Project02.py
```

On some systems, you can also use:

```bash
python Project02.py
```

## 💻 Example

When the program starts, it displays:

```text
===================================
        WELCOME TO CLOVER SHOP
===================================

Available product

1. Rice    N50,000
2. Chicken   N8,000
3. Cooking oil  N12,000
4. Sugar     N5,000
5. Milk     N4,000
```

The user can then select a product and enter the desired quantity.

For example:

```text
Choose a product
>> 1

Provide quantity
>> 2

You bought 2 Rice
Cost: N100000
```

The program then asks whether the user wants to purchase another product.

## 📄 Project Structure

```text
.
├── Project02.py
└── README.md
```

## 🎯 Purpose

The purpose of this project is to strengthen my understanding of Python fundamentals by building a small interactive program from scratch.

This project focuses on understanding how different Python concepts can be combined to create a functional command-line application.

## 🚧 Possible Future Improvements

Some possible improvements for future versions include:

* Allowing users to purchase more than two products
* Reducing repeated code
* Using dictionaries to store products and prices
* Adding better input validation
* Improving the shopping cart system
* Adding stock management
* Creating a cleaner receipt system
* Allowing users to remove or change items in their cart
* Adding a proper checkout process

## 📚 Learning Project

This is a beginner learning project and is intentionally kept simple. It represents my progress while learning Python programming and applying fundamental concepts through practical projects.

## 👤 Author

**Ahmad Nasir**
