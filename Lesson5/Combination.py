# age = 20
# has_ticket = True

# # BOTH must be true
# if age >= 18 and has_ticket:
#     print("Welcome!")

# # AT LEAST ONE must be true
# if age < 12 or age > 65:
#     print("Discount price")

# requirement user :
# if person is age 18 year old and has ticket we will welcome to the join movie 
# person need smaller then 12 or longer 65 we'll discount 

age = int(input("Input age ")) # default input from key is string # declare is datatype int
# string age casting to int
has_ticket = True # datatype is boolean
can_join ="we will welcome to the join movie" # data is string 
has_discount = 'well discount' # datatype string 

# Logical and, or ,not

if age >=18 and has_ticket : # statment check if person is age 18 year old and has ticket
    print(can_join)
if age <12 or age > 65 :
    print(has_discount)