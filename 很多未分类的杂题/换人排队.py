n,d=map(int,input().split())
high=[0]*n
for i in range(n):
    high[i]=int(input())
highs=sorted(high)
def ifcanchange(a):
    k=0
    while True:
        if a-highs[k]<=d:
            for m in high[:high.index(highs[k])]:
                if abs(m-highs[k])>d:
                    k+=1
                    break
                highs.remove(highs[k])
                return k
        else:
            k+=1
def replace(k,x):
    m=high[x]
    high[high.index(highs[k])]=m
    high[x]=highs[k]

for x in range(n):
    replace(ifcanchange(x),x)
print(high)

