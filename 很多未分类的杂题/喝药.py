n=int(input())
s=list(map(int,input().split()))
nums=[0]*n
po=[[float('-inf'),float('-inf')]]*n
bo=0
if s[0]>=0:
    nums[0]=s[0]
    bo=1
for i in range(1,n):
    if s[i]>=0:
        bo+=1
        nums[i]=nums[i-1]+s[i]
    else:
        nums[i]=nums[i-1]
        po[i]=[i,s[i]]
po.sort(key=lambda y:-y[1])
for x in po:
    if x==[float('-inf'),float('-inf')]:
        break
    if nums[x[0]]+x[1]>=0:
        bo+=1
        for j in range(x[0],n):
            nums[j]+=x[1]
            if nums[j]<0:
                bo-=1
                for t in range(x[0],j+1):
                    nums[t]-=x[1]
                break
print(bo)

#贪心加后悔
import heapq


def max_potions(n, potions):
    # 当前健康值
    health = 0
    # 已经饮用的药水效果列表，用作最小堆
    consumed = []

    for potion in potions:
        # 尝试饮用当前药水
        health += potion
        heapq.heappush(consumed, potion)
        if health < 0:
            # 如果饮用后健康值为负，且堆中有元素
            if consumed:
                health -= consumed[0]
                heapq.heappop(consumed)


    return len(consumed)

n = int(input())
potions = list(map(int, input().split()))
print(max_potions(n, potions))