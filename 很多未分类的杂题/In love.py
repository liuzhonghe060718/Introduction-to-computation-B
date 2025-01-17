import heapq
from collections import defaultdict
q=int(input())
numsx,numsd=[],[]
count=defaultdict(int)
heapq.heapify(numsx)
heapq.heapify(numsd)
for _ in range(q):
    s=list(input().split())
    num1=(int(s[1]),int(s[2]))
    num2=(-int(s[1]),-int(s[2]))
    if s[0]=='+':
        count[num1]+=1
        heapq.heappush(numsx,num1)
        heapq.heappush(numsd,num2)
    else:
        count[num1]-=1
    if not numsd and not numsx:
        a, b = numsx[0], (-numsd[0][0], -numsd[0][1])
        while count[a] == 0:
            heapq.heappop(numsx)
            a = numsx[0]
        while count[b] == 0:
            heapq.heappop(numsd)
            b = (-numsd[0][0], -numsd[0][1])
    if len(numsd) > 1 and len(numsx) > 1 and numsx[0][1] < -numsd[0][0]:
        print("Yes")
    else:
        print("No")

