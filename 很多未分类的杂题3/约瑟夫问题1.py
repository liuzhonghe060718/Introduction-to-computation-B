while True:
    n,m=map(int,input().split())
    if n==0:
        break
    else:
        monkeys=list(range(0,n))
        location=0
        while len(monkeys)>1:
            location=(location+m-1)%(len(monkeys))
            monkeys.pop(location)
        print(monkeys[0]+1)