
def f(n,x,y,dm):
    if n==1:
        dm[x][y]=' '
    else:
        l=3**(n-2)
        f(n-1,x,y,dm)
        f(n-1,x+l,y,dm)
        f(n-1,x+2*l,y,dm)
        f(n - 1, x, y+l, dm)
        f(n - 1, x+l, y+2*l, dm)
        f(n - 1, x+2*l, y+l, dm)
        f(n - 1, x, y+2*l, dm)
        f(n - 1, x+2*l, y+2*l, dm)
        for i in range(x+l,x+2*l):
            for j in range(y+l,y+2*l):
                dm[i][j]='X'
def main():
    n = int(input())
    t=3**(n-1)
    dp=[[' 'for i in range(t)]for _ in range(t)]
    f(n,0,0,dp)
    print('+'*(t+2))
    for row in dp:
        print('+'+''.join(row)+'+')
    print('+'*(t+2))
if __name__=="__main__":
    main()