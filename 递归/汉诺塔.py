m=int(input())
def change(n,from_,to_,help_):
    if n==1:
        print(f'{from_}->{to_}')
    else:
        change(n-1,from_,help_,to_)
        print(f'{from_}->{to_}')
        change(n-1,help_,to_,from_)
print(2**m-1)
change(m,'A','B','C')


