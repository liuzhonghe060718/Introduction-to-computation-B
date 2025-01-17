n,m=map(int,input().split())
graph={i:[] for i in range(n)}

matrix2=[[0for _ in range(n)] for _ in range(n)]
for  _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    matrix2[a][b]=1
    matrix2[b][a]=1
for i in range(n):
    s=[0 for _ in range(n)]
    for j in range(n):
        if i==j:
            s[j]+=len(graph[i])
        s[j]-=matrix2[i][j]
    print(' '.join(map(str,s)))