n,m=map(int,input().split())
cost=[0]*n
for i in range(n):
    cost[i]=int(input())
def check(x):
    current=0
    k=1
    for j in range(n):
        if current+cost[j]>x:
            k+=1
            current=cost[j]
            if k>m:
                return False
        else:
            current+=cost[j]
    return True


left, right = max(cost), sum(cost)  # 下界是数组的最大值，上界是数组的总和

while left < right:
    mid = (left + right) // 2  # 当前尝试的最大组和

    if check(mid):
        right = mid  # 缩小上界
    else:
        left = mid + 1  # 增大下界
print(left)