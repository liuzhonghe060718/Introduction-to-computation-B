n,m,l=map(int,input().split())
graph={i:[]for i in range(n)}
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
start=int(input())
for i in range(n):
    graph[i].sort()
visited=set()
def dfs(x,steps,answer):
    if x not in answer:
        answer.append(x)
    visited.add(x)
    if steps>=l:
        return
    for y in graph[x]:
        if y not in visited:
            dfs(y,steps+1,answer)
    return answer
print(' '.join(map(str,dfs(start,0,[]))))
