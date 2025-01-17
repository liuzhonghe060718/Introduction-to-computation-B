n,w=map(int,input().split())
candy=[]
values,k=0,0
for _ in range(n):
    v,m=map(int,input().split())
    x=v/m
    candy.append([x,v,m])
while w>0 and k<n:
    candy.sort(key=lambda x: x[0],reverse=True)
    t=min(w,candy[k][2])
    w-=t
    values+=candy[k][0]*t
    k += 1
print(f"{values:.1f}")