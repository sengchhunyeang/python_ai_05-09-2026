#conditional satement : using for check condition 
# from exercises.solutions.lesson2_variables_solution import score


student_name1 = input("Student_name1 :")
student_name2= input("Student_name2 :")
score_studentname1 =float(input("input score "))# history subject 
score_studentname2 = float(input("input score"))
print(f"studentname1:,{student_name1} ,Scrore : {score_studentname1}")
if score_studentname1 >=75 : # 75 ->100 false 
    print("A")
elif score_studentname1 >=60 : # 60 -> 61-62 -63 > 74
    print("B")
elif score_studentname1 >=50: # 50 -> 59
    print("C")
elif score_studentname1 >=40: #40 -> 49
    print("D")
elif (score_studentname1,student_name2) >=30: #30 -> 39
    print("E")
else : 
    print("your score under 30 Fail")
