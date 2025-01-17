n=int(input())
s,t=0,0
for i in range(1,n+1):
    N=list(str(i))
    t+=i**2
    if i%7==0:
        s+=i**2
    else:
        for k in N:
            if k=="7":
                s+=i**2
                break

print(t-s)