import math
    # 预处理所有可能的平方数
squares = set()
i = 1
while i * i <= 10 ** 9:
    squares.add(i * i)
    i += 1
a=input()
n=len(a)
def dfs(x,y):
    p=int(a[x:y])
    if p in squares:
        if y==n:
            return True
        else:
            if dfs(y,n):
                return True
    else:
        if x==y-1:
            return False
        if dfs(x,n-1):
            return True
    return False
if a in squares:
    print('Yes')
else:
    print('Yes'if dfs(0,n)else 'No')


def is_blessed_id(A):
    # 预处理所有可能的平方数
    squares = set()
    i = 1
    while i * i <= 10 ** 9:
        squares.add(i * i)
        i += 1

    # 将数字A转换为数字列表
    digits = list(map(int, str(A)))

    # DFS函数，判断是否可以分割成平方数
    def dfs(idx):
        if idx == len(digits):
            return True

        num = 0
        for i in range(idx, len(digits)):
            num = num * 10 + digits[i]
            if num in squares:
                if dfs(i + 1):
                    return True
        return False

    # 调用DFS函数，判断是否可以分割成平方数
    return "Yes" if dfs(0) else "No"


# 读取输入
A = int(input())
# 输出结果
print(is_blessed_id(A))



