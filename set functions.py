l=[1,1,1,2,3,3,4,5]

#remove duplicates
s=set(l)
print(list(s))


l=[1,1,1,2,3,3,4,5]
#remove duplicates without using set()
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)


#print common elements in a list
l1=[23,45,78,90,12,74]
l2=[45,89,23,56,34]
s1=set(l1)
s2=set(l2)
a=s1.intersection(s2)
print(list(a))
