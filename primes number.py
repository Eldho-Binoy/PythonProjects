num=int(input("enter the num: "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("Neihgter prime noe composite")