k=int(input())
for _ in range(k):
    n=int(input())
    s=[]
    for i in range(n):
        s.append(list(input()))
    r,b=0,0
    for x in range(n):
        for y in range(n):
            if s[x][y]=='r'and s[x-1][y]!='r' and s[x][y-1]!='r':
                r+=1
            if s[x][y] == 'b' and s[x - 1][y] != 'b' and s[x][y - 1] != 'b':
                b+=1
    print(r,b)