s=[]
n=int(input())
x=n*n
while len(s)<x:
    a=list(map(int,input().split()))
    s.extend(a)
matrix=[list(row)for row in zip(*[iter(s)]*n)]
def find(lis):
    dp = [0 for _ in range(n)]
    dp[0]=lis[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+lis[i],lis[i])
    return max(dp)
answer=[]
for i in range(n):
    used=[0for _ in range(n)]
    for j in range(i,n):
        l=[used[k]+matrix[j][k]for k in range(n)]
        used=l
        answer.append(find(l))
print(max(answer))