n=int(input())
s=sorted(list(map(int,input().split())))
k,b=[],set()
for i in s:
    if i>n:
       k.append(i)
a,c=set(s),set(k)
for j in range(1,n+1):
    b.add(j)
answer=sorted(b-(a-c))
print(' '.join(str(m)for m in answer))
print(' '.join(str(m)for m in k))