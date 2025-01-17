from math import log
t=int(input())
for i in range(t):
    n=int(input())
    print((n+1)*n//2-2**(int(log(n,2))+2)+2)
