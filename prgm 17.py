#define a func takes string as arguments ans return anew dictionary where keys are words and values are length of each word.
#call func and print dic
l="python coding is easy and fun"
new=l.split()
print(new)
d={}
def fun1(new,d):
   # d={i:len(i) for i in new }
    for i in new:
       d[i]=len(i)
    return d
a=fun1(new,d)
print(a)