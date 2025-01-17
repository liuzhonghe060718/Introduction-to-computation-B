n=int(input())
x=0
for i in range(n):
    k=list(map(int,input().split()))
    if sum(k)>1:
        x+=1
print(x)
