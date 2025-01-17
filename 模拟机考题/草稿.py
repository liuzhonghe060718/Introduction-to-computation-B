n=int(input())
time=[[] for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    time[i]=[a,b]
if n==1:
    print(time[0][0]+time[0][1])
    exit()
time.sort(key=lambda x:(x[1],-x[0]),reverse=True)
ans=time[0][0]
k=1
le=time[0][1]
while k<n-1:
    if le>=time[k][0]:
        ans+=time[k][0]
        le=le-time[k][0]+time[k][1]
        k+=1
    else:
        ans+=time[k][0]
        le=time[k][1]
        k+=1
ans+=max(le,time[k][1]+time[k][0])
print(ans)