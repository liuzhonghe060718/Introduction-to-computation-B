n,m=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))

a,b=0,0
s=[]
while a<n or  b<m:
    if a>=n and b<m:
        break
    if a<n and b>=m:
        s.extend(s1[a:])
        break
    x,y=s1[a],s2[b]
    if x<y:
        s.append(x)
        a+=1
    elif y<x:
        b+=1
    else:
        a+=1
        b+=1
print(' '.join(map(str,s)))