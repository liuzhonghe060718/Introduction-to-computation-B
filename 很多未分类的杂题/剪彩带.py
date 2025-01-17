result=[]
def check(n,a,b,c,t):
    if n<min(a,b,c):
        t=0
    else:
        if n==a or n== b or n==c:
            result.append(t+1)
        check(n-a,a,b,c,t+1)
        check(n-b,a,b,c,t+1)
        check(n-c,a,b,c,t+1)
n,a,b,c=map(int,input().split(" "))
check(n,a,b,c,0)
result.sort(reverse=True)
print(result[0])





