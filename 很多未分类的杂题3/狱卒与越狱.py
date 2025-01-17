x=int(input())
def m(a):
    if a==0:
        return 1
    else:
        return 0
for _ in range(x):
    n=int(input())
    prison=[1]*n
    for i in range(2,n+1):
        for k in range(1,n+1):
            if k%i==0:
                prison[k-1]=m(prison[k-1])
    print(prison.count(1))
