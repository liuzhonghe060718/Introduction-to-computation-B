n,q=map(int,input().split())
a,b=[0]*q,[0]*q
for i in range(q):
    x,y=map(int,input().split())
    a[i],b[i]=x,y
def m(q,a,b):
    for i in range(q):
        try:
            if b[a.index(b[a.index(b[i])])]==a[i]:
                return 'Yes'
            else:
                continue
        except:
            continue
    return 'No'
print(m(q,a,b))
