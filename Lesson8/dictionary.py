# dictionary
student = {
    # "key" : value
    "name": "Touch Rufa",
    "age": 20,
    "grade": "A",
}
# call by key for show value 
print(f"name a student {student['grade']}")
# call dictionary
# print(student.get("name"))

# add dictionary
student["gender"] = "Male" # if no key is adding 
print("after add :", student)
student["age"] = 30 # if has already key is updating
print("after update :", student)