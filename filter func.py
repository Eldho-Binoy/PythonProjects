l=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2==0,l)))
print(list(map(lambda x:x%2==0,l)))

l=[23,65,89,12,20,33,85,40]
#filter elements greater than 50
print(list(filter(lambda x:x>50,l)))
print(list(map(lambda x:x>50,l)))


#even values less than 50
print(list(filter(lambda x:x<50 and x%2==0,l)))

fruits=['apple','orange','pineapple','grapes','avacado']

#elements whoes len is grater than 5
print(list(filter(lambda x:len(x)>5,fruits)))