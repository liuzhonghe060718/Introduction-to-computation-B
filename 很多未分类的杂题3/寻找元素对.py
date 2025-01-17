n=int(input())
numbers=sorted(list(map(int,input().split())))
K=int(input())
answer=0
for i in numbers[0:int(n/2)+1]:
    if K-i in numbers:
        answer+=1
print(answer)
