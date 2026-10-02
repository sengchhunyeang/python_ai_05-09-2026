multiple = int(input("input mutiple :"))
number = 1 # 1+2=3+2=5+2=7+2=9
index = int(input("input index :"))
while number <= index:  # 9 <= 8 ? flase 
    resule = multiple * number
    print(f"{multiple}*{number}={resule}")
    number += 2 # number + 1 = 1+1 =2 1+6
