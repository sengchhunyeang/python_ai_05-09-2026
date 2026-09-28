# Simple calculator using input() and operators
# input() always returns text (string), so we convert with float()

print("=" * 40)
print("CALCULATOR")
print("=" * 40)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

print("=" * 40)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "//":
    result = num1 // num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    result = None
    print("Invalid operator")

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
