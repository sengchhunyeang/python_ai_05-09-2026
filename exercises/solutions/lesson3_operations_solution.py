# ============================================================
# LESSON 3: Operations, Concatenation & Type Checking — SOLUTIONS
# ============================================================


# --------------------------------------------------
# Task 3.1 — String concatenation
# --------------------------------------------------
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)


# --------------------------------------------------
# Task 3.2 — String concatenation with date
# --------------------------------------------------
day = "21"
month = "September"
year = "2026"
date = day + " " + month + " " + year
print("Today is", date)


# --------------------------------------------------
# Task 3.3 — Integer addition
# --------------------------------------------------
A = 15
B = 25
print("A + B =", A + B)


# --------------------------------------------------
# Task 3.4 — Float operations
# --------------------------------------------------
price = 9.99
quantity = 4
total = price * quantity
print("Total price: $" + str(total))


# --------------------------------------------------
# Task 3.5 — Type checking practice
# --------------------------------------------------
print(type("Hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type(0))         # <class 'int'>


# --------------------------------------------------
# Task 3.6 — Mixed operations
# --------------------------------------------------
# Fixed: convert integer to string first
print("I am " + str(25) + " years old")


# --------------------------------------------------
# Task 3.7 — Calculator
# --------------------------------------------------
num1 = 15
num2 = 4

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)


# --------------------------------------------------
# Task 3.8 — Type conversion
# --------------------------------------------------
number_str = "100"
number_int = int(number_str)
result = number_int + 50
print("Result:", result)


# --------------------------------------------------
# Task 3.9 — Boolean operations
# --------------------------------------------------
is_raining = True
is_sunny = False

print("Raining AND Sunny:", is_raining and is_sunny)  # False
print("Raining OR Sunny:", is_raining or is_sunny)    # True
print("NOT Raining:", not is_raining)                  # False


# --------------------------------------------------
# Task 3.10 — Mini project: Receipt generator
# --------------------------------------------------
item_name = "Laptop"
item_price = 899.99
quantity = 2
total = item_price * quantity

print("=================================")
print("RECEIPT")
print("Item:", item_name)
print("Price: $" + str(item_price))
print("Quantity:", quantity)
print("Total: $" + str(total))
print("=================================")
