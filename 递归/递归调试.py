n=int(input())
def fei(n,k):
    print(' '*(4*k)+f'n={n}')
    if n<=2:
        return 1
    else:
        return fei(n-1,k+1)+fei(n-2,k+1)

fei(n,0)