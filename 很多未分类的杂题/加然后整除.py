import math
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    x=math.ceil(a/b)
    print(b*x-a)
