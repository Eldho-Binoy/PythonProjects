# l=[1,1,2,3,4,5,5,5,6,7]

#create new dictionary where keys are numbers and values are count of each number
# new={1:456,"tyu":6}
# for i in l:
#     new[i]=l.count(i)
# print(new)


# l=[34,12,56,89,90,11]
# #find the largest, second largest, smallest, second smallest element
# print(l)
# print(max(l))
# print(min(l))
# l.sort()
# print(l)
# print(l[1])
# print(l[-2])


#create a new list of salary and new list of age
#find max salary and min age
l=[["arun",23,40000],["amal",24,50000],["anu",27,30000]]
age=[]
salary=[]
for i in l:
    age.append(i[1])
    salary.append(i[2])
print(salary)
print(age)
print("Max salary ",max(salary))
print("min age",min(age))