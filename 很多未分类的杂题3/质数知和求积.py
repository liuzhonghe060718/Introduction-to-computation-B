s=int(input())
def oula(r):
    prime=[0 for i in range(r+1)]
    common=[]
    for i in range(2,r+1):
        if prime[i]==0:
            common.append(i)
        for j in common:
            if i*j>r:
                break
            prime[i*j]=1
            if i%j==0:
                break
    return common
q=oula(10000)
k=int(s/2)
while s-k not in q or k not in q:
    k-=1
print(k*(s-k))
