n=int(input())
answer=[]
def back(idx1,idx2,path):
    global answer
    if idx2+idx1==2*n:
        if idx2==n and idx1==n:
            answer.append(path[:])
        return
    if idx1>idx2:
        back(idx1+1,idx2,path+['('])
        back(idx1,idx2+1,path+[')'])
    elif idx2==idx1:
        back(idx1+1,idx2,path+['('])

back(0,0,[])
answer.sort()
for i in answer:
    print(''.join(i))