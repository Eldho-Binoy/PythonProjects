# l=[1,2,3,4]
# #create dictionary where keys are numbers and values are squares of numbers
# new={i:i**2 for i in l}
# print(new)
#
# #dictionary where keys are numbers and values are cube of numbers
# new={i:i**3 for i in l}
# print(new)

# l=[10,20,30,40]
# #create new dict where keys are index and values are numbers
# new={i:l[i] for i in range(0,len(l))}
# print(new)
s="python coding is easy and fun"
#new dict where key is word and value is length
new={i:len(i) for i in s.split()}
print(new)