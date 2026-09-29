#multiplication table
n=int(input("Enter the number"))
i=1
while(i<=n and i<=10):
    print(end="\n")
    print(n,"*",i,"=",n*i,end="    ")
    count = n // 10
    k=10
    while(count!=0 and (k+i)<=n):
        print(n,"*",k+i,"=",(n*(k+i)),end="    ")
        count-=1
        k+=10
    i+=1