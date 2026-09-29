# def add():
#     n1=int(input("enter num1: "))
#     n2=int(input("Enetr num2: "))
#     s=n1+n2
#     print(s)
#
# add()

#define to display " helo your name"
# def fun1():
#     a=str(input("Enter you name: "))
#     print(f"Hello {a}")
#     return
#
# fun1()

#function to find count of specific character
# def fun2():
#     b=str(input("Enter the string: "))
#     a=str(input("Enter the charcter: "))
#     count=0
#     for i in b:
#         if(i==a):
#             count+=1
#     print(count)
#     return
# fun2()

#function to find factorial of a number
# def fun3():
#     a=int(input("enter the number"))
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print(fact)
#     return
#
# fun3()


# #function to check whether a number is amstrong
# def fun4():
#     a=int(input("Enter the number: "))
#     b=str(a)
#     l=len(b)
#     s=0
#     for i in b:
#         s=s+(int(i)**l)
#     if(a==s):
#         print("Armstrong")
#     else:
#         print("not armstrong")
# fun4()

#function to check prime or not
# def fun5():
#     n=int(input("Enter the num: "))
#     for i in range(2,n//2):
#         if(n%i==0):
#             print("Not prime")
#             break
#     else:
#         print("prime")
#     return
# fun5()



#define a fun to find factors of a numbers
# def fun6():
#     n=int(input("input the num: "))
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
#     return
# fun6()

########################################################
#sum of two num
# def fun7(n1,n2):
#     s=n1+n2
#     print("sum: ",s)
# fun7(6,7)
########################################################

#func to find simple interest dynamic
# def simpleinterest():
#     p=int(input("ENter the principal akount: "))
#     y=int(input("enter the year: "))
#     r=float(input("Enter the rate: "))
#     s=p*y*r/100
#     print("Simpleinterest is: ", s)
# simpleinterest()

#define a fun that takes string and a character and print count of characters in string
# def fun8(n,a):
#     count=0
#     for i in n:
#         if i==a:
#             count+=1
#     print(count)
# n=str(input("Enter string: "))
# a=str(input("entr the char: "))
# fun8(n,a)

#return value sum
# def fun9(a,b):
#     sum=a+b
#     return sum
# a=int(input("enter the num: "))
# b=int(input("Enter num: "))
# n=fun9(a,b)
# print(n)


#define func that takes 3 num and return product as result .
# def product(a,b,c):
#     product=a*b*c
#     return product
# a=int(input("Enter num: "))
# b=int(input("Enter num: "))
# c=int(input("Enter num: "))
# n=product(a,b,c)
# print(n)