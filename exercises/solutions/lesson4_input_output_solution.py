# ============================================================
# LESSON 4: Input and Output — SOLUTIONS
# ============================================================


# --------------------------------------------------
# Task 4.1 — Basic input
# --------------------------------------------------
name = input("Enter your name: ")
print("Hello, " + name + "!")


# --------------------------------------------------
# Task 4.2 — Input and greet
# --------------------------------------------------
name = input("Enter your name: ")
city = input("Enter your city: ")
print("Hello " + name + " from " + city + "!")


# --------------------------------------------------
# Task 4.3 — Input age (with type conversion)
# --------------------------------------------------
age = int(input("Enter your age: "))
print("You are", age, "years old.")


# --------------------------------------------------
# Task 4.4 — Simple calculator with input
# --------------------------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)


# --------------------------------------------------
# Task 4.5 — Personal info form
# --------------------------------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
job = input("Enter your job: ")
city = input("Enter your city: ")

print("=================================")
print("PROFILE")
print("Name:", name)
print("Age:", age)
print("Job:", job)
print("City:", city)
print("=================================")


# --------------------------------------------------
# Task 4.6 — Temperature converter
# --------------------------------------------------
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(str(celsius) + "°C = " + str(fahrenheit) + "°F")


# --------------------------------------------------
# Task 4.7 — Mad Libs game
# --------------------------------------------------
noun = input("Enter a noun (person): ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")

print("The " + adjective + " " + noun + " likes to " + verb + " in " + place + ".")


# --------------------------------------------------
# Task 4.8 — Student registration system
# --------------------------------------------------
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_gpa = float(input("Enter student GPA: "))

print("=================================")
print("REGISTRATION SUCCESSFUL")
print("Student:", student_name)
print("Age:", student_age)
print("GPA:", student_gpa)
print("Status: Registered")
print("=================================")


# --------------------------------------------------
# Task 4.9 — Shopping receipt
# --------------------------------------------------
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = item_price * quantity

print("=================================")
print("RECEIPT")
print("Item:", item_name)
print("Price: $" + str(item_price))
print("Quantity:", quantity)
print("Total: $" + str(total))
print("=================================")


# --------------------------------------------------
# Task 4.10 — Mini project: User profile builder
# --------------------------------------------------
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
hobby = input("Enter your favorite hobby: ")

bmi = weight / ((height / 100) ** 2)
bmi = round(bmi, 2)

print("=================================")
print("USER PROFILE")
print("Name:", first_name, last_name)
print("Age:", age)
print("Height:", height, "cm")
print("Weight:", weight, "kg")
print("BMI:", bmi)
print("Hobby:", hobby)
print("=================================")
