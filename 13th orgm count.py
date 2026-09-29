#count of three digit nubers that has "3"
# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if "3" in s:
#         count+=1
#     i+=1
# print(count)



#count of numbers divisible by 7 and 3 range(200,300)
# count=0
# i=200
# while(i<=300):
#     if(i%7==0 and i%3==0):
#         count+=1
#     i+=1
# print(count)



#count of odd numbers divisible by 5 in range (1,100)
# count=0
# i=1
# while(i<=100):
#     if(i%5==0):
#         count+=1
#     i+=2
# print(count)



#count of palindrome numbers in range(1,1000)
# count=0
# i=1
# while(i<=1000):
#     k=str(i)
#     if(k==k[::-1]):
#         count+=1
#     i+=1
# print(count)



#count number divisible by 3 in range(1,50)
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         count+=1
#     i+=1
# print(count)



#sum of frst 5 numbers
# i=1
# s=0
# while(i<=5):
#     s+=i
#     i+=1
# print(s)



#sum of numbers divisible by 3 in range (1,50)
# s=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         s+=i
#     i+=1
# print(s)



#sum of all 3 digit numbers
# s=0
# i=100
# while(i<=999):
#     s+=i
#     i+=1
# print(s)



#sum of frst 10 even numbers
# s=0
# i=0
# while(i<=20):
#     if(i%2==0):
#         s+=i
#     i+=1
# print(s)


#product of series 1,2,3,4,5
# product=1
# i=1
# while(i<=5):
#     product*=i
#     i+=1
# print(product)



#product of frst 10 odd numbers
# p=1
# i=1
# while(i<=20):
#     p*=i
#     i+=2
# print(p)



#product of numbers that has "3" in range(1,50)
# p=1
# i=1
# while(i<=50):
#     s=str(i)
#     if("3" in s):
#         p*=i
#     i+=1
# print(p)



#find factorial of input number
# factorial=1
# i=int(input("eter a number"))
# n=1
# while(n<=i):
#     factorial*=n
#     n+=1
# print(f"{i}! is {factorial}")



#multiplication table
# n=int(input("Enter the number"))
# i=1
# while(i<=10):
#     print(f"{n}*{i}={n*i}")
#     i+=1



#Sum of digits of number
n=int(input("Enter the numb"))
s=0
while(n>0):
    d=n%10
    s+=d
    n//=10
print(s)