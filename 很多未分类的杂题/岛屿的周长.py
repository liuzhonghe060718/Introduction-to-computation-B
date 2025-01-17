n,m=map(int,input().split())
a=[0 for i in range(m+4)]
s=[a,a]
for i in range(n):
    s.append([0,0]+list(map(int,input().split()))+[0,0])
s.append(a)
s.append(a)
k=0
for x in range(1,n+3):
    for y in range(1,m+3):
        if s[x][y]==0:
            if s[x][y-1]==1:
                k+=1
            if s[x+1][y]==1:
                k+=1
            if s[x][y+1]==1:
                k+=1
            if s[x-1][y]==1:
                k+=1
print(k)
