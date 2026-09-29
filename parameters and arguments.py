#Positional Arguments
# def fun1(a,b):
#     print("name",a)
#     print("age",b)
# fun1("Arun",67)

#keyword Arguments
# def fun1(a,b):
#     print("name",a)
#     print("age",b)
# fun1(a="Arun",b=67)
# fun1(b=67,a="arun")

#default Argumnets
# def fun1(a,b=23):
#     print(a,b)
# fun1("arun")
# fun1("Arun",45)


#variable lenght
def fun2(*args):
    print(args)
    print(type(args))
fun2(12,23,45)


def fun3(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun3(a="10",b=89,x=99)

#define func to find sum of 2 num using arbitary positional arguments
def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4,5,7)
add(1,2,3)