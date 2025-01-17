p=int(input())
price=sorted(list(map(int,input().split())))
k=0
while price:
    while p>=price[0] :
        p-=price.pop(0)
        k+=1
        if not price:
            break
    if k>0  and len(price)>=2:
        k-=1
        p+=price.pop(-1)
    else:
        break
print(k)


