n=int(input())
gas=[]
for _ in range(n):
    gas.append(tuple(map(int,input().split())))
l,p=map(int,input().split())
gas.sort(reverse=True)
now_right=l-p
now_pos=l
can_reach=l-p
ga=p
next_pos=0
ans=0
for i in range(n):
    if gas[i][0]>=now_right:
        if can_reach<=l-(ga+gas[i][1]):
            next_pos=i
            can_reach=l-(ga+gas[i][1])
    else:
        ans+=1
        now_pos=next_pos
        now_right=can_reach
        ga+=gas[next_pos][1]
        if now_right<=0:
            break
print(ans)


