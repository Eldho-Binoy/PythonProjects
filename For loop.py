# s="hello"
# for i in s:
#     print(i)


#print sum of numbers in list[56,89,34,10]
# s=0
# l=[56,89,34,10]
# for i in l:
#     s+=i
# print(s)



#check palindrome
# s=str(input("Enter the string"))
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# if(rev==s):
#     print(s,"is Palindrome ")
# else:
#     print("Not palindrome")



#reverse a number
# n=1086
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)



l=[12,34,56,45,89,16,69,33]

#print each num in a list
# for i in l:
#     print(i)


#print even value
# for i in l:
#     if(i%2==0):
#         print(i)


#num divisible by 5
# for i in l:
#     if(i%5==0):
#         print(i)


#number contain "3"
# for i in l:
#     string=str(i)
#     p=0
#     for k in string:
#         if(k=="3"):
#             p=1
#     if(p!=0):
#         print(i)


#count of even numbers in a list
# count=0
# for i in l:
#     if(i%2==0):
#         count+=1
# print(count,"even numbers")


#print square of each number
# for i in l:
#     print(i**2)


l=[12,4.5,6.8,30,"arun","hello"]

#print only float point values
# for i in l:
#     if(type(i)==float):
#         print(i)


d={'a':23,'b':25,'c':28,'d':30,'e':22}

#even values
# for i in d:
#     if(d[i]%2==0):
#         print(d[i])


colors=['red','green','blue','orange','black']

#even values
# for i in colors:
#     print("first letter is ",i[0])
# for i in colors:
#     print("Last letter : ",i[-1])
# for i in colors:
#     print("reverse is",i[::-1])

#all colors with "b"
# for i in colors:
#     if("b" in i):
#         print(i)
#