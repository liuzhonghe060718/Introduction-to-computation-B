t=int(input())
for _ in range(t):
    e,f=map(int,input().split())
    weigh=f-e
    n=int(input())
    s=[[]]*n
    for i in range(n):
        a,b=map(int,input().split())
        s[i]=[a,b]
    dp=[float('inf')]*(weigh+1)
    dp[0]=0
    for j in range(1,weigh+1):
        for x in s:
            if x[1]<=j:
                dp[j]=min(dp[j],dp[j-x[1]]+x[0])
    k=dp[-1]
    if k==float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {k}.')