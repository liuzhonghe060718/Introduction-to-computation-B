m=int(input())
def fei(n):
    if n==1 or n==2:
        return 1
    return fei(n-1)+fei(n-2)
if m<=2:
    print(1)
else:
    print(fei(m))
