t,k=map(int,input().split())
s=[]
mol=1000000007
b0=0
for _ in range(t):
    a,b=map(int,input().split())
    s.append([a,b])
    b0=max(b0,b)
dp=[0for _ in range(b0+1)]
arr=[0for _ in range(b0+1)]
for y in range(k):
    dp[y]=1
    arr[y]=y+1
dp[k]=dp[k-1]+2
arr[k-1]=arr[k-2]+dp[k-1]
for i in range(k,b0+1):
    dp[i]=(dp[i-1]+dp[i-k])%mol
    arr[i]=arr[i-1]+dp[i]
for a,b in s:
    print((arr[b]-arr[a-1])%mol)
