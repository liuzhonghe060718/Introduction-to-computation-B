def check(a,b):
    if b >= 2 * a:
        return True
    else:
        b-=a
        if check(b,a):
            return False
        else:
            return True

while True:
    try:
        a1,b1=sorted(list(map(int,input().split())))
    except EOFError:
        break
    if a1 == b1 == 0:
        break
    print('win'if check(a1,b1) else 'lose')