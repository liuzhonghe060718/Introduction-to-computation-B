n=int(input())
s=[[0for i in range(n)]for _ in range(n)]
k=1
p=[]
for i in range(n):
    p.extend([i,n-i-1,n-i-1,i])
for i in range(2*n-1):
    if i%4==0:
        for j in range(n):
            if s[p[i]][j]==0:
                s[p[i]][j]=k
                k+=1
    elif i%4==1:
        for j in range(n):
            if s[j][p[i]]==0:
                s[j][p[i]]=k
                k+=1
    elif i%4==2:
        for j in range(n-1,-1,-1):
            if s[p[i]][j]==0:
                s[p[i]][j]=k
                k+=1
    else:
        for j in range(n-1,-1,-1):
            if s[j][p[i]]==0:
                s[j][p[i]]=k
                k+=1
for x in s:
    print(' '.join(map(str,x)))


def generate_spiral_matrix(n):
    # 初始化一个 n x n 的矩阵
    matrix = [[0] * n for _ in range(n)]
    idx = 1

    def fill_matrix(x, y, size):
        nonlocal idx
        if size == 0:
            return
        if size == 1:
            matrix[x][y] = idx
            idx += 1
            return

        # 填充最上边的行
        for j in range(y, y + size - 1):
            matrix[x][j] = idx
            idx += 1

        # 填充最右边的列
        for i in range(x, x + size - 1):
            matrix[i][y + size - 1] = idx
            idx += 1

        # 填充最下边的行
        for j in range(y + size - 1, y, -1):
            matrix[x + size - 1][j] = idx
            idx += 1

        # 填充最左边的列
        for i in range(x + size - 1, x, -1):
            matrix[i][y] = idx
            idx += 1

        # 递归填充内圈
        fill_matrix(x + 1, y + 1, size - 2)

    # 从左上角 (0, 0) 开始填充
    fill_matrix(0, 0, n)
    return matrix


n = int(input())
result = generate_spiral_matrix(n)
for row in result:
    print(" ".join(map(str, row)))