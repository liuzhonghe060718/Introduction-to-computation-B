import heapq
from collections import defaultdict
pig=[]
weight=[]
used=defaultdict(int)
while True:
    try:
        s=input()
    except EOFError:
        break
    if s=='min':
            while weight:
                x=heapq.heappop(weight)
                if not used[x]:
                    print(x)
                    heapq.heappush(weight,x)
                    break
    elif s=='pop' :
        if weight:
            used[pig.pop()] += 1
    else:
        s=int(s[5:])
        pig.append(s)
        heapq.heappush(weight,s)



import heapq
from collections import defaultdict

out = defaultdict(int)
pigs = []
pigs_stack = []

while True:
    try:
        s = input()
    except EOFError:
        break

    if s == "pop":
        if pigs_stack:
            out[pigs_stack.pop()] += 1
    elif s == "min":
        if pigs_stack:
            while True:
                x = heapq.heappop(pigs)
                if not out[x]:
                    heapq.heappush(pigs, x)
                    print(x)
                    break
                out[x] -= 1
    else:
        y = int(s.split()[1])
        pigs_stack.append(y)
        heapq.heappush(pigs, y)
