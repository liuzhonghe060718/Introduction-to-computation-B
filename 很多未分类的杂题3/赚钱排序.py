n=int(input())
List=input().split()
end=[]
t=1
if n!=1:
    for x in range(0,n-1):
        if int(List[x])<=int(List[x+1]):
            t+=1
            end.append(t)
        else:
            end.append(t)
            t=1
    print(max(end))
else:
    print(1)