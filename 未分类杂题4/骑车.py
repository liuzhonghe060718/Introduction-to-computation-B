import math

while True:
    n = int(input())
    if n==0:
        break
    else:
        riders=[]
        for _ in range(n):
            v,t=map(int,input().split(    ))
            if t<0:
                continue
            riders.append(math.ceil(t+(4500/v)*3.6))
        print(min(riders))


