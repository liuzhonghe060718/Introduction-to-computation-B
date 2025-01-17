n=int(input())
s1=list(map(int,input().split()))
s=sorted(s1,key=lambda x:s1.index(x)-x)
k=0
la,ra,ri=-1,-1,0
for i in range(n):
    if i-s[i]<=ra+1:
        ri=max(ri,i+s[i])
        if ri>=n-1:
            k+=1
            break
    else:
        k+=1
        la=ra
        ra=ri
        if i-s[i] <= la + 1:
            ra = max(ra, i+s[i])
            if ra >= n - 1:
                k+=1
                break
print(k)
