n,m=map(int,input().split())
house=[]
for _ in range(n):
    house.append(tuple(map(int,input().split())))
k=0
end=0

house.sort(key=lambda x:x[0]-x[1])
while end<m:
    ra=m+1
    for i in house:
        if i[0]>=end:
            ri=max(end,i[0]-i[1]+1)+i[1]
            if ri<ra:
                ra=ri
                ji=i
    try:
        house.remove(ji)
        k+=1
        end=ra
        ji=None
    except ValueError:
        break
print(k)

