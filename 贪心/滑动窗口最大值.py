import heapq
from collections import defaultdict
count=defaultdict(int)
n,k=map(int,input().split())
nums=list(map(int,input().split()))
s=nums[:k].copy()
for x in range(k):
    s[x]=-s[x]
    count[s[x]]+=1
heapq.heapify(s)
ans=[0 for _ in range(n-k+1)]
ans[0]=-s[0]
for i in range(n-k):
    count[-nums[i]]-=1
    heapq.heappush(s,-nums[i+k])
    count[-nums[i+k]]+=1
    a=s[0]
    while count[a]<=0:
        heapq.heappop(s)
        a=s[0]
    ans[i+1]=-a
print(' '.join(map(str,ans)))






