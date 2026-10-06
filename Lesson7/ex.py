# Student Score Calculator

print("=" * 30)  # style
count_subject = int(input("How Many Subject You Have ? :"))
print("=" * 30)  # style
# Ctrl+D 
# list to store scores
scores = []

# output the number of subjects
print(f"Your Subject Have : {count_subject}")
# ff = 1
for i in range(count_subject): # rang(start,stop)
    score = float(input(f"Enter Your Score {i + 1}: "))
    scores.append(score)

# # output the scores
# print("\nYour Score Have :")
# for j in range(count_subject):
#     print(f"Your Score {j + 1} Is : {scores[j]}")

# # calculate total and average
total = sum(scores)
av = total / count_subject
print(f"Your Total is{total}")
# print(f"Hello1 Hello2")
# pri# # Calculate grade based on aver
if av >= 85:
    grade = "A"
elif av >= 75:
    grade = "B"
elif av >= 65:
    grade = "C"
elif av >= 50:
    grade = "D"
else:
    grade = "F"

# # output the results
print(f"\nYour Total Is : {total}")
print(f"Your Average Is : {av:.2f}")
print(f"Your Grade Is : {grade}")

# ctr+?