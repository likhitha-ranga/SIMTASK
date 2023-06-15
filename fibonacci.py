def fib(a,b):
    c=a+b
    print(c)
    return b,c
n=int(input("enter the no.of fibonacci numbers"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    (a,b)=fib(a,b)
