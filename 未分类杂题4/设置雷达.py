import math
m=1

def number_leida(n,d,islands):
        s=[[0]]*n
        k=1
        if d<=0:
            return -1
        for i in range(n):
            if islands[i][1]>d:
                return -1
            else:
                b=math.sqrt(d*d-islands[i][1]**2)
                s[i]=[islands[i][0]-b,islands[i][0]+b]
        s.sort(key=lambda x:x[0])
        if not s:
            return -1
        for i in range(n-1):
            if s[i][1]>=s[i+1][0]:
                s[i+1][1]=min(s[i][1],s[i+1][1])
            else:
                k+=1
        return k
while True:
    p,q=map(int,input().split())
    if q==p==0:
        break
    ranges=[]
    for i in range(p):
        a, b = map(int, input().split())
        ranges.append([a,b])
    print(f'Case {m}: {number_leida(p,q,ranges)}')
    m+=1
    input()

