n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
ans=0
def bo(x,y,k):
    global ans
    if (k==-1 and n%2==1) or (n%2==0 and k==0):
        pass
    elif k==1:
        ans=max(matrix[x][y],ans)
    else:
        su=0
        for i in range(k):
            su+=(matrix[x][y+i]+matrix[x+i][y]+matrix[x+k-1][y+i]+matrix[x+i][y+k-1])
        su-=(matrix[x][y]+matrix[x+k-1][y]+matrix[x][y+k-1]+matrix[x+k-1][y+k-1])
        ans=max(ans,su)
        bo(x+1,y+1,k-2)
bo(0,0,n)
print(ans)