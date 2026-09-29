# # # Q1.Define a function that takes 2 numbers and returns their product
# def fun1(a,b):
#     sum=a*b
#     return sum
# a=int(input("enter num: "))
# b=int(input("enter num : "))
# n=fun1(a,b)
# print(n)
#
# # Q2.Define a function that takes a string and returns number of vowels
# def fun2(n):
#     count=0
#     a="AEIOUaeiou"
#     for i in n:
#         if i in a:
#             count+=1
#     return count
# n=str(input("Enetr string; "))
# a=fun2(n)
# print(a)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     area=l*b
#     return area
# l=int(input("Enetr length"))
# b=int(input("enter breadth"))
# a=area(l,b)
# print(a)



# # # Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# l=[45,78,90,12,35]
# l2=[]
# def fun4(l,l2):
#     for i in l:
#         if(i%2==0):
#             l2.append(i)
#     print(l2)
# fun4(l,l2)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# new=[]
# def fun5(l,new):
#     for i in l:
#         n=str(i)
#         sum=0
#         for j in n:
#             sum+=int(j)
#         new.append(sum)
#     print(new)
# fun5(l,new)
#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
# new=[]
# def fun6(l,new):
#     for i in l:
#         count=0
#         for j in l:
#             if i==j:
#                 count+=1
#         if count==1:
#             new.append(i)
#     print(new)
# fun6(l,new)
#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# new=[]
# def fun7(list1,list2,new):
#     for i in list1:
#         for j in list2:
#             if(i==j):
#                 new.append(i)
#     print(new)
# fun7(list1,list2,new)