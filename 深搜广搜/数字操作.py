from collections import deque
n1=int(input())
def bfs(n):
    stocks=deque([(1,0)])
    used=[False]*(n+1)
    while stocks:
        num,steps=stocks.popleft()
        if num<=n and not used[num]:
            if num==n:
                return steps
            steps+=1
            stocks.append((num*2,steps))
            stocks.append((num+1,steps))
            used[num]=True
print(bfs(n1))
