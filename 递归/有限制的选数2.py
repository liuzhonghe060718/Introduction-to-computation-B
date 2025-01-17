n,k=map(int,input().split())
result=0
nums=list(map(int,input().split()))
def back(idx,sm):
    global result
    if idx==n:
        if sm==k:
            result+=1
        return
    for i in range((k-sm)//nums[idx]+1):
        back(idx+1,sm+i*nums[idx])
    return
back(0,0)
print(result)