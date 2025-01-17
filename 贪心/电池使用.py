while True:
    try:
        n=int(input())
    except EOFError:
        break
    time=sorted(list(map(int,input().split())))
    s=sum(time)/2
    if s<time[-1]:
        answer=s*2-time[-1]
    else:
        answer=s
    print('%.1f' % (answer))


