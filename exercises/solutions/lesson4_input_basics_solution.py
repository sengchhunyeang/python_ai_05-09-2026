# ============================================================
# LESSON 4: Input Basics (Simple) — SOLUTIONS
# ============================================================


# --------------------------------------------------
# Task 1 — Say hello
# --------------------------------------------------
name = input("What is your name? ")
print("Hello " + name + "!")


# --------------------------------------------------
# Task 2 — Ask two things
# --------------------------------------------------
name = input("What is your name? ")
color = input("What is your favorite color? ")
print(name + " likes " + color + ".")


# --------------------------------------------------
# Task 3 — Ask age
# --------------------------------------------------
age = input("How old are you? ")
print("You are " + age + " years old.")


# --------------------------------------------------
# Task 4 — Simple math
# --------------------------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)


# --------------------------------------------------
# Task 5 — Your info
# --------------------------------------------------
name = input("Name: ")
age = input("Age: ")
school = input("School: ")

print("--- Your Info ---")
print("Name:", name)
print("Age:", age)
print("School:", school)
