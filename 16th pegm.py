#space pattern
k=3*2
for i in range(1,5):
    for j in range(1,k+1):
        print(end=" ")
    for p in range(1,i+1):
        print("*",end=" ")
    k-=2
    print()


#pyramid
k=3*2
for i in range(1,5):
    for j in range(1,k+1):
        print(end=" ")
    for p in range(1,i+1):
        print("*",end="   ")
    k-=2
    print()



for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for m in range(3,0,-1):
    for n in range(1,m+1):
        print("*",end=" ")
    print()


k=3*2
for i in range(1,5):
    for j in range(1,k+1):
        print(end=" ")
    for m in range(1,i+1):
        print("*",end=" ")
    k-=2
    print()
k=2
for n in range(3,0,-1):
    for h in range(1,k+1):
        print(end=" ")
    for l in range(1,n+1):
        print("*",end=" ")
    print()
    k+=2



k=3*2
for i in range(1,5):
    for j in range(1,k+1):
        print(end=" ")
    for m in range(1,i+1):
        print("*",end="   ")
    k-=2
    print()
k=2
for n in range(3,0,-1):
    for h in range(1,k+1):
        print(end=" ")
    for l in range(1,n+1):
        print("*",end="   ")
    print()
    k+=2



n=ord('E')
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(n),end=" ")
    n-=1
    print()



for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()



for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()



