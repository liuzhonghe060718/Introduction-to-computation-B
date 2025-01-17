T=int(input())
for _ in range(T):
    n=int(input())
    s=list(map(int,input().split()))
    l=[[0,0] for _ in range(n)]
    for i in range(2*n):
        if i%2==0:
            l[i//2][0]=s[i]
        else:
            l[(i-1)//2][1]=s[i]
    l.sort()
    l=list(map(tuple,l))
    used=set()
    k=0
    for i in range(n):
        if l[i] not in used:
            la=l[i]
            k+=1
            used.add(la)
            for j in range(i+1,n):
                if l[j] not in used and [j][0]>=la[0] and l[j][1]>=la[1]:
                    used.add(l[j])
                    la=l[j]
        if len(used)==n:
            break
    print(k)

