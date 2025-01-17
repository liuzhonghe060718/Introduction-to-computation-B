def zuhe(nums,k):
    def dfs(idx):
        if len(path)==k:
            result.append(path[:])
            return
        if idx<n:
            path.append(nums[idx])
            dfs(idx+1)
            path.pop()
            dfs(idx+1)
    n=len(nums)
    result,path=[],[]
    dfs(0)
    result.sort(key=lambda x:(len(x),x))
    return result
n,k=map(int,input().split())
num=list(map(int,input().split()))
for x in zuhe(num,k):
    print(' '.join(map(str,x)))