n=int(input())
s=[]
k=1
for i in range(n):
    a,b=map(int,input().split())
    s.append((a,b))
s.sort(key=lambda x:(x[1],x[0]))
m=s[0][1]
for x in range(1,n):
    if s[x][0]>m:
        k+=1
        m=s[x][1]
print(k)