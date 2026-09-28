# ============================================================
# LESSON 2: Variables and Data Types — SOLUTIONS
# ============================================================


# --------------------------------------------------
# Task 2.1 — Create a string variable
# --------------------------------------------------
name = "Alice"
print(name)


# --------------------------------------------------
# Task 2.2 — Create an integer variable
# --------------------------------------------------
age = 20
print("I am", age, "years old")


# --------------------------------------------------
# Task 2.3 — Create a float variable
# --------------------------------------------------
balance = 250.75
print("My account balance is $", balance)


# --------------------------------------------------
# Task 2.4 — Create a boolean variable
# --------------------------------------------------
is_student = True
print("Am I a student?", is_student)


# --------------------------------------------------
# Task 2.5 — Check the type of each variable
# --------------------------------------------------
my_string = "Hello"
my_int = 42
my_float = 3.14
my_bool = True

print(type(my_string))   # <class 'str'>
print(type(my_int))       # <class 'int'>
print(type(my_float))     # <class 'float'>
print(type(my_bool))      # <class 'bool'>


# --------------------------------------------------
# Task 2.6 — Fix invalid variable names
# --------------------------------------------------
# 1st_name → first_name (cannot start with number)
first_name = "Alice"

# $price → price (cannot use special characters)
price = 100

# my-age → my_age (cannot use hyphen)
my_age = 20

print(first_name)
print(price)
print(my_age)


# --------------------------------------------------
# Task 2.7 — Variable reassignment
# --------------------------------------------------
score = 100
print("Original score:", score)

score = 95
print("Updated score:", score)


# --------------------------------------------------
# Task 2.8 — Multiple variables in one line
# --------------------------------------------------
x, y, z = 10, 20, 30
print("x =", x, "y =", y, "z =", z)


# --------------------------------------------------
# Task 2.9 — Swap variables
# --------------------------------------------------
a = 5
b = 10
print("Before swap: a =", a, "b =", b)

# Python swap trick
a, b = b, a
print("After swap: a =", a, "b =", b)


# --------------------------------------------------
# Task 2.10 — Student profile
# --------------------------------------------------
student_name = "Sokha"
student_age = 21
gpa = 3.8
is_enrolled = True

print("=================================")
print("Student:", student_name)
print("Age:", student_age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)
print("=================================")
