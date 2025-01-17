import math
n=int(input())
a,b=map(int,input().split())
nums=[]
for _ in range(n):
    nums.append(list(map(int,input().split())))
nums.sort(key=lambda x:x[0]*x[1])
j=a
answer=0
for i in range(n):
    answer=max(answer,j//nums[i][1])
    j=j*nums[i][0]
print(answer)