n=int(input())
s=[[0]]*n
for i in range(n):
    s[i]=list(map(int,input().split()))
s.reverse()
for i in range(1,n):
    for j in range(len(s[i])):
        s[i][j]=max(s[i-1][j],s[i-1][j+1])+s[i][j]
print(s[-1][0])