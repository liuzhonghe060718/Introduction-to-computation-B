n=int(input())
boxes=sorted(list(map(int,input().split())))
boxs=list(set(boxes))
kinds=[0]*len(boxs)
for i in range(len(boxs)):
    kinds[i]=boxes.count(boxs[i])
while len(kinds)>1:
    a=max(kinds.pop(0),kinds.pop(0))
    kinds.insert(0,a)
print(kinds[0])




