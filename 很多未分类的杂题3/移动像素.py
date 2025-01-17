n,m,k=map(int,input().split())
move=[]
for _ in range(k):
    move.append(list(map(int,input().split())))
def m(moves):
    for i in moves:
        a,b,c=[i[0],i[1]+1],[i[0]+1,i[1]],[i[0]+1,i[1]+1]
        if a in moves and b in moves and c in moves:
            answer_1=[moves.index(a),moves.index(b),moves.index(i),moves.index(c)]
            return max(answer_1)+1
    return 0
print(m(move))




n, m, k = map(int, input().split())
moves = [tuple(map(int, input().split())) for _ in range(k)]
painted = set()  # 用于记录黑色像素


def check_loss(i, j, painted):
    # 检查以(i, j)为右下角的2x2方块
    return (
            (i, j) in painted and
            (i - 1, j) in painted and
            (i, j - 1) in painted and
            (i - 1, j - 1) in painted
    )


for move_number in range(1, k + 1):
    i, j = moves[move_number - 1]

    # 涂黑当前像素
    painted.add((i, j))

    # 检查以(i, j)为右下角的2x2方块
    if check_loss(i, j, painted):
        print(move_number)  # Pasha在此回合输掉
        break
else:
    print(0)  # 没有输掉
