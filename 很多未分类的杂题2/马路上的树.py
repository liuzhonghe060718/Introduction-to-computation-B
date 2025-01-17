l,m=map(int,input().split())
cut=set()
for _ in range(m):
    a,b=map(int,input().split())
    cut.update(range(a,b+1))
print(l-len(cut)+1)
