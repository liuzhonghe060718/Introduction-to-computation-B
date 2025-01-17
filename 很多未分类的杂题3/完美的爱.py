n=int(input())
values=list(map(int,input().split()))
h=[0]*n
h[0]=values[0]-520
max_len=0
for x in range(1,n):
    h[x]=h[x-1]+values[x]-520
for i in range(n-1,-1,-1):
    a=h.index(h[i])
    if a<i:
        max_len=max(max_len,i-a)
    if h[i]==0:
        max_len=max(max_len,1)
print(max_len*520)



