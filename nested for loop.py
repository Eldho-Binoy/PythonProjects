# l=[10,20,30,40]
# for i in l:
#     for k in range(1,4):
#         print(i,end=" ")
#     print()




# for i in range(1,4):
#     for k in range(1,4):
#         print(i,end=" ")
#     print()


# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()


#
# l=[['lion','tiger'],['cat','elephnt']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)


# n=['kelly','alan','jenny']
# for i in n:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


#
# n=[1,2,3]
# qns=['what','when','why']
# for i in n:
#     print(i)
#     for j in qns:
#         print(j,end=" ")
#     print()



# d=[{'id':101,'name':'arun','age':25},{'id':102,'name':'amal','age':23},{'id':103,'name':'anu','age':24}]
# for i in d:
#     for j in i:
#         print(i[j],end=" ")
#     print()



# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()




for i in range(2,9,2):
    for j in range(1,5):
        print(i,end=" ")
    print()



for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()


for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


for i in range(1,5):
    for j in range(1,5):
        if(i==j):
            print(j,end=" ")
        else:
            print("0",end=" ")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        if(j%2==0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()


a=0
for i in range(1,5):
    for i in range(i):
        a += 1
        print(a,end=" ")
    print()



for i in range(1,8,2):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


print("pyramid")
n=5
m=(n//2)+1
o = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==m):
            print("*", end=" ")
        elif(j<m and j>(m-0)):
            print("*",end=" ")
        elif(j>m and j<=(m+o)):
            print("*", end=" ")
        else:
            print(end=" ")
    o+=1
    print()

#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k+=1
#     print()
#
#
#
# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()



