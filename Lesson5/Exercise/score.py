st_n1 = input("enter student name1: ")
st_n2 = input("enter student name2: ")
score_1 = float(input("enter score st_n1: "))
score_2 = float(input("enter score st_n2: "))
if score_1 >= 90:
    print(f"Student Name1: {st_n1}, Score:{score_1}, Grade: A")
elif score_1 >=80:
    print(f"Student Name1: {st_n1}, Score: {score_1}, Grade: B")
elif score_1 >= 70:
    print(f"Student Name1: {st_n1}, Score: {score_1}, Grade: C")
elif score_1 >= 60:
    print(f"Student Name1: {st_n1}, Score: {score_1}, Grade: D") # work ...something else 
elif score_1 >= 50:
    print(f"Student Name1: {st_n1}, Score: {score_1}, Grade: E")
else:
    print(f"Student Name1: {st_n1}, Score: {score_1}, Grade: F, Fail")

if score_2 >= 90:
    print(f"Student Name2: {st_n2}, Score:{score_2}, Grade: A")
elif score_2 >=80:
    print(f"Student Name2: {st_n2}, Score: {score_2}, Grade: B")
elif score_2 >= 70:
    print(f"Student Name2: {st_n2}, Score: {score_2}, Grade: C")
elif score_2 >= 60:
    print(f"Student Name2: {st_n2}, Score: {score_2}, Grade: D")
elif   score_2>= 50:
    print(f"Student Name2: {st_n2}, Score: {score_2}, Grade: E")
else:
    print(f"Student Name2: {st_n2}, Score: {score_2}, Grade: F; Fail")
