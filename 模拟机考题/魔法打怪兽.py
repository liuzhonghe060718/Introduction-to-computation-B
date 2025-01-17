n,w=map(int,input().split())
p=sum(map(int,input().split()))
guai=[]
ans=0
idx=0
for _ in range(n):
    guai.append(tuple(map(int,input().split())))
guai.sort(key=lambda x:x[1])
while w>0 and idx<=n-1:
    if p>=guai[idx][0] and w>=guai[idx][1]:
        ans+=1
        w-=guai[idx][1]
    idx+=1
print(ans)
