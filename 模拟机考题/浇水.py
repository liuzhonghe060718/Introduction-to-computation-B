n,a,b=map(int,input().split())
water=list(map(int,input().split()))
i,j=0,n-1
ans=0
wa,wb=a,b
while i<=j:
    if i==j:
        if wa<wb:
            if wb < water[j]:
                ans += 1
                wb = b
            wb-=water[i]
        else:
            if wa < water[i]:
                ans += 1
                wa = a
            wa-=water[i]
    else:
        if wa < water[i]:
            ans += 1
            wa = a
        if wb < water[j]:
            ans += 1
            wb = b
        wa-=water[i]
        wb-=water[j]
    i+=1
    j-=1
print(ans)