from collections import defaultdict
m,n=map(int,input().split())
dire=[(0,1),(0,-1),(1,0),(-1,0)]
input()
input()
k=0
matrix=[[[]for _ in range(n)]for _ in range(m)]
count=defaultdict(int)
for i in range(m):
    for j in range(n):
        try:
            matrix[i][j]=list(map(int,input().split()))
            count[sum(matrix[i][j])]+=1
        except EOFError:
            continue
for x in range(m):
    for y in range(n):
        ans=False
        for dx,dy in dire:
            nx,ny=dx+x,dy+y
            if 0<=nx<m and 0<=ny<n and matrix[nx][ny]==matrix[x][y]:
                ans=True
                break
        if ans:
            k+=1
MAX=m*n*0.4
su=0
p=0
sorted_dict = {key: count[key] for key in sorted(count,reverse=True)}
for i in sorted_dict.keys():
    su+=sorted_dict[i]
    if su>MAX:
        break
    p+=1
print(f'{k} {p}')

