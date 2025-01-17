n,k=map(int,input().split())
nums=list(map(int,input().split()))
result=0
def back(idx,sm,path,answer):
    global result
    if idx==n:
        if sm==k and path not in answer:
            answer.append(path[:])
            result+=1
        return
    sm+=nums[idx]
    back(idx+1,sm,path+[nums[idx]],answer)
    sm-=nums[idx]
    back(idx+1,sm,path,answer)
    return
back(0,0,[],[])
print(result)
