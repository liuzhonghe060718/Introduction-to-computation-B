n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a,b=0,0
s=[]
while a<n and  b<m:
    x,y=A[a],B[b]
    if x>y:
        s.append(y)
        b+=1
    else:
        s.append(x)
        a+=1
while a<n:
    s.append(A[a])
    a+=1
while b<m:
    s.append(B[b])
    b+=1
print(' '.join(map(str,s)))