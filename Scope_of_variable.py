x=10
def f():
    print("Inside",x)
f()
print("outside",x)

x=10
def f():
    x=8
    print("Inside",x)
f()
print("outside",x)