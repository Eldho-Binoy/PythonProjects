#printeven num
# l=[23,65,42,80,56,41]
# for i in l:
#     if(i%2==0):
#         print(i)


#print primes
# for i in l:
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)



#print all primes in range(1,100)
# for i in range(2,101):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)


#find armstrong range(100,1000)
for i in range(100,1001):
    a=str(i)
    l=len(a)
    s=0
    for j in a:
        n=int(j)
        s=s+(n**l)
    if(s==i):
        print(i)
