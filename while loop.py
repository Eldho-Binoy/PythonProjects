#program to print first 10 integers
# i=0
# while(i<10):
#     print(i+1,end=" ")
#     i+=1



#program to print frst 10 even numbers

# i=2
# while(i<=20):
#     print(i, end=" ")
#     i+=2



#print frst 10 odd numbers

# i=1
# while(i<=19):
#     print(i, end=" ")
#     i+=2



#print 1,4,7,10,13,16 and 10,20,30,40,50,60 and 3,6,9,12,15,18,21 and 5,4,3,2,1
# i=1
# while(i<=16):
#     print(i,end= " ")
#     i+=3
#
# i=10
# while(i<=60):
#     print(i,end=" ")
#     i+=10
#
# i=3
# while(i<=21):
#     print(i,end=" ")
#     i+=3
#
# i=5
# while(i>=1):
#     print(i,end=" ")
#     i-=1

# print 8,6,4,2,0 and 100,101,102,.....,200 and all 4 digit numbers
# i=8
# while(i>=0):
#     print(i,end=" ")
#     i-=2
#
# i=100
# while(i<=200):
#     print(i,end=" ")
#     i+=1
#
# i=1000
# x=0
# while(i<=9999):
#  #   print(i,end="\n")
#     x+=1
#     i+=1
# print(x)



#print 3 digit numbers divisible by 3
# i=100
# while(i<=999):
#     if(i%3==0):
#         print(i,end=" ")
#     i+=1



#print 4 digit numbers where digit 3 is present
# i=1000
# while(i<=9999):
#     if("3" in str(i)):
#         print(i, end=" ")
#     i+=1
#


#print number divisible by 3 and 5  i range (1,100)
# i=1
# while(i<=100):
#     if(i%5==0 and i%3==0):
#         print(i,end=" ")
#     i+=1





#print square from 1 to 10
# i=1
# while(i<=10):
#     print(i**2,end=" ")
#     i+=1


#print primes in range(1,100)
i=2
count=99
while(i<=100):
    m=2
    value="prime"
    while(m<=(i//2) and m!=1):
        if(i%m==0):
            value="not prime"
        m+=1
    if value=="not prime":
        count-=1
    print(f"{i} is {value}")
    i+=1
print( count)

