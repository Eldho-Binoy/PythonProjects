#program to calculate electricity bill based on the folowwing critiria
#Units Consumed      Rates/Unit
# 0-100               0rs/unit
# 100-200             5rs/unit
# 200-300             10rs/unit
# above 300           15rs/unit


# n=int(input("Enter the units used"))
# if(n<=100):
#     print("Bill =", n*0)
# elif(n<=200):
#     print(f"Bill = {5*(n-100)}")
# elif(n<=300):
#     print(f"Bill = {(5*100)+(10*(n-200))}")
# else:
#     print(f"Bill = {(5*100)+(10*100)+(15*(n-300))}")





#CHECK whether the user entrred numer is 2 digit/3 digit /4 digit number

# n=int(input("enter the numb"))
# if(n>9 and n<100):
#     m="2 digit"
# elif(n>99 and n<1000):
#     m="3 digit"
# elif(n>999 and n<10000):
#     m="4 digit"
# else:
#     m="above 4 digits or below 2 digit"
# print(m)




#Make calculator (+,-,*,/,//,%)

# n1=int(input("Enter the frst num"))
# o=str(input("Enetr the operator"))
# n2=int(input("enter secnd num"))
# if(o=="+"):
#     n3=n1+n2
# elif(o=="-"):
#     n3=n1-n2
# elif(o=="*"):
#     n3=n1*n2
# elif(o=="/"):
#     n3=n1/n2
# elif(o=='//'):
#     n3=n1//n2
# else:
#     n3=n1%n2
# print(f"{n1}{o}{n1} = {n3}")



#print how many days in a month

n=str(input("Enter the month"))
a=["january","march","may","july","august","october","december"]
b="february"
if(n in a):
    dates=31
elif(n in b):
    dates="29 or 28"
else:
    dates=30
print(f"{dates} days present")



#print grade based on critiria
#  Marks        Grade
# 91-100          A
# 81-90           B
# 71-80           C
# 61-70           D
# Below 61        E

