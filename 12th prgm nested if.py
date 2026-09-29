#To chck whether user entered num is a positive even or odd/ negative even

# n=int(input("enter num"))
# if(n>0):
#     if(n%2==0):
#         type="positive even"
#     else:
#         type="positive odd"
# else:
#     if(n%2==0):
#         type = "negative even"
#     else:
#         type="negative odd"
# print(type)



#check whether a number is divisible by 2 and 3, divisible by 2 and not by 3, divisible by 3 and not by 2, not divisibke by 2 and 3

n=int(input("Enter the num"))
if(n%2==0):
    print("divisible by 2")
    if(n%3==0):
        print(" and 3")
    else:
        print(" but not by 3")
else:
    print("Not divisible by 2")
    if(n%3==0):
        print(" but divisible by 2")
    else:
        print("and 3")
