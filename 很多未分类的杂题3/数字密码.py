import math
n=int(input())
x=[]
for a in range(1,n):
    for b in range(1,n-a):
        c=n-a-b
        if a!=b and b!=c and c!=a:
            x.append(math.gcd(a,(math.gcd(b,c))))
print(max(x))


你自己写的啥玩意，太占空间了，看看下面这个
n=int(input())
i = 1 + 2 + 3
while n%i != 0:
    i += 1
else:
    print(n // i)
