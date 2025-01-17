n,k=[int(m) for m in input().split()]
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    s.pop(0)
    a.extend(s)
b=set(a)
if sum(b)==int((k+1)*k/2):
    print("YES")
else:
    print("NO")
