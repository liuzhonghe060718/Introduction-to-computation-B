n=int(input())
s=sorted(list(tuple(map(int,input().split()))for _ in range(n)),key=lambda x:(x[1],x[0]))
i,k=1,0
last_back=s[0][1]
for i in range(1,len(s)):
    if s[i][0]>=last_back:
        k+=1
        last_back=s[i][1]
print(k)