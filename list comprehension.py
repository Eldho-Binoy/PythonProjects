# l=[1,2,3,4]
# #new list with squares
# new=[i**2 for i in l]
# print(new)
#
# #new lis =t with cubes
# new=[i**3 for i in l]
# print(new)
#
# new=[5 for i in l]
# print(new)
#
# l=[23,46,55,11,78,90,24]
#
# #create new list with even values
# new=[i for i in l if i%2==0]
# print(new)
#
#
# #new liat with num greater t han 50
# new=[i for i in l if i>50]
# print(new)
#
#
# colors=['red','green','blue','orange','black']
#
# #create new list with frst letter of each color
# new=[i[0] for i in colors]
# print(new)
#
# #new list with length of each color
# new=[len(i) for i in colors]
# print(new)
#
# #new list with sqauree roots of
# l=[25,36,81,100]
# new=[int(i**0.5) for i in l]
# print(new)
#
# #create new list of last letters
# new=[i[-1] for i in colors]
# print(new)
#
#
# #reverse of each element
# new=[i[::-1] for i in colors]
# print(new)
#
# l=[23,78,12,56]
# new=[i+10 for i in l]
# print(new)
#
# l=[{'empid':101,"name":'arun','salary':20000,"email":'arun@gmail.com'},
#    {'empid':102,"name":'amal','salary':25000,"email":'amal@gmail.com'},
#    {'empid':103,"name":'anu','salary':30000,"email":'anu@gmail.com'}]
# new=[i['email'] for i in l]
# print(new)
#
#
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

#create list of strings
# new=[i for i in l if type(i)==str]
# print(new)
# #create list of float
# new=[i for i in l if type(i)==float]
# print(new)
# #create list of positive num
# new=[i for i in l if (type(i)==int or type(i)==float) and  i>0]
# print(new)

# fruits=['apple','orange','pineapple','avocado','grapes']
#
# #new list with length greater than 6
# new = [i for i in fruits if len(i)>6]
# print(new)
#
#
# #new list with values divisible by 3 in  range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)
#
# s="python coding is easy and fun"
#
# #new list with only vowels
# new=[i for i in s if i in "AEIOUaeiou"]
# print(new)
