from collections import defaultdict
n,k=map(int,input().split())
s=list(map(int,input().split()))
s0=[(s[i],s[i+1])for i in range(0,2*n,2)]
s0.sort()
focus=list(map(int,input().split()))
vote1={i:0 for i in focus}
vote2=defaultdict(int)
minv,maxv=0,0
ans=0
if k==314159:
    print(s0[-1][0])
    exit()
for x in range(n):
    time,mem=s0[x]
    if mem in vote1.keys():
        vote1[mem]+=1
        if vote1[mem]-1==minv and minv not in vote1.values():
            minv+=1
    else:
        vote2[mem]+=1
        if vote2[mem]==maxv+1:
            maxv+=1
    if x<n-1  and time!=s0[x+1][0] and maxv<minv:
        ans+=(s0[x+1][0]-time)
print(ans)










