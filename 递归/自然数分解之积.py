def m(n):
    if n==1:
        return 1
    else:
        answer=0
        for i in range(1,n):
            answer=max(answer,m(n-i)*i)
        a=n//2
        return max(answer,a*(n-a))
n=int(input())
print(m(n))