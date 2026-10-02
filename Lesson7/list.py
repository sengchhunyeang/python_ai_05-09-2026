from datetime import date 
import calendar
# list declaration ?
# erorr syntax f format can not use in list
fruit = [
    "Apple",
    "Orange",
    "Water melon",
    "banana",
    "tragon",
    "cococut",
]  # list of fruit
# list item how to count by index 0,1,2
# print(fruit[2])

# access item
print(fruit[0])

# slicing
print(fruit[3:])  # [index : lastitem ]

today = date.today()
print(today)


print(calendar.month(2026, 11))
