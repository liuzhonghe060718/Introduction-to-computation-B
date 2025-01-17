while True:
    n=int(input())
    if n==0:
        break
    o=0
    s=[0]*n
    for i in range(n):
        p,y=map(int,input().split())
        s[i]=(p,y)
    j=sorted(s,key=lambda x:(x[0],x[1]),reverse=True)
    f=sorted(s,key=lambda x: x[1])
    print(j,f)
    for i in range(n):
        k=j.index(f[i])
        a,b,c,d=set(f[:i]),set(f[i+1:]),set(j[:k]),set(j[k+1:])
        if a<=c and b>=d:
            o+=1
    print(o)


while True:
    n=int(input())
    if n==0:
        break
    s=[tuple(map(int,input().split())) for _ in range(n)]
    s.sort(key=lambda x:(x[0],x[1]))
    c=1
    m=s[0][1]
    for i in range(n):
        if s[i][1]<m:
            c+=1
            m=s[i][1]
    print(c)