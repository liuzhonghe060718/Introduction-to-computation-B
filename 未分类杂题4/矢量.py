n=int(input())
a,b,c=0,0,0
for i in range(1,n+1):
    d,e,f=input().split()
    a+=int(d)
    b+=int(e)
    c+=int(f)
if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")