import heapq
from collections import defaultdict
n,k=map(int,input().split())
s=list(map(int,input().split()))
s0=[(s[i],s[i+1])for i in range(0,2*n,2)]
s0.sort()
focus=list(map(int,input().split()))
end=0
vote=defaultdict[int]
rank=[[0,i]for i in range(314159)]
heapq.heapify(rank)
while end<n-1:
    t,v=s0[end]
    end+=1
    vote[v]+=1
    while s0[end][0]==t:
        end+=1
        vote[s0[end][1]]+=1
    large=[]
    x=heapq.nlargest(k+1,rank)
    for _ in range(k):

    for i in x:
        i[0]=vote[i[1]]







