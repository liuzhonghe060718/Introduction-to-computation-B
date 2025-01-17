n=int(input())
def sorting(x):
    if x==1:
        return [[1]]
    else:
        s=sorting(x-1)
        s_1=[]
        for j in s:
             for i in range(x):
                 s_1.append(j[:i]+[x]+j[i:])
        s=s_1
        return s
m=sorted(sorting(8))
def is_valid_queen_placement(board):
    main_diag = set()
    anti_diag = set()
    for i in range(8):
        a=i+1 - board[i]
        b=i+1 + board[i]
        if a in main_diag or b in anti_diag:
            return False
        main_diag.add(a)
        anti_diag.add(b)
    return True
t,p=[0]*92,0
for q in m:
    if is_valid_queen_placement(q):
        t[p]=''.join(map(str,q))
        p+=1
for _ in range(n):
    l=int(input())
    print(t[l-1])


