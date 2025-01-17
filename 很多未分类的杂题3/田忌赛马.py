
while True:
    n=int(input())
    k=0
    if n==0:
        break
    tian=sorted(list(map(int,input().split())))
    king = sorted(list(map(int, input().split())))
    lTian = 0
    rTian = n - 1
    lKing = 0
    rKing = n - 1
    ans = 0
    while lTian <= rTian:
        if tian[lTian] > king[lKing]:
            ans += 1
            lTian += 1
            lKing += 1
        elif tian[rTian] > king[rKing]:
            ans += 1
            rTian -= 1
            rKing -= 1
        else:
            if tian[lTian] < king[rKing]:
                ans -= 1

            lTian += 1
            rKing -= 1

    print(ans * 200)


#
from bisect import bisect_left
while True:
    n=int(input())
    k=0
    if n==0:
        break
    tian=sorted(list(map(int,input().split())))
    kings = sorted(list(map(int, input().split())))
    ping=[]
    for h in tian:
        a=bisect_left(kings,h)
        if a:
            k+=1
            kings.pop(a-1)
        else:
            ping.append(h)
    for i in range(len(ping)):
        if ping[i]<kings[i]:
            k-=1
    print(k*200)