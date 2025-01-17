n=int(input())
values=sorted(list(map(int,input().split())),reverse=True)
money,my,k=sum(values),0,0
while my*2<=money:
    my+=values[k]
    k+=1
print(k)
