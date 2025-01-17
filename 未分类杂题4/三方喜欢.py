def love() :
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    q = int(data[1])
    exists=[[False]*(n+1) for _ in range(n+1)]
    index=2
    for _ in range(q):
        a=int(data[index])
        b=int(data[index+1])
        index+=2
        exists[a][b]=True
        for c in range(q):
            if exists[b][c]==True and exists[c][a]==True:
                return "Yes"
    return 'No'
print(love())

