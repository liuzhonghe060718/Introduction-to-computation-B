from functools import cmp_to_key
m=int(input())
n=int(input())
nums=list(input().split())
def compare(a,b):
    return int(b+a)-int(a+b)
nums.sort(key=cmp_to_key(compare))
c=min(m,sum(map(len,nums)))
for i in range(n):
    nums[i]=[nums[i],len(nums[i])]
result=0
def dfs(path,k,idx):
    global result
    if k>=c or idx==n:
        if k==c:
            result=''.join(path)
        return
    if result:
        return
    dfs(path+nums[idx][0],k+nums[idx][1],idx+1)
    dfs(path,k,idx+1)
dfs('',0,0)
print(result)






