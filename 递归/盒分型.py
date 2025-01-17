k=int(input())
def put(n):
    if n==1:
        return 'X'
    else:
        l = 3 ** (n - 2)
        result1,result2,result3='','',' '*l
        for l1,l2 in zip(put(n-1).split('\n'),put(n-1).split('\n')):
            result1+=l1+result3+l2+'\n'
        for x in put(n-1).split('\n'):
            result2+=result3+x+result3+'\n'
        return result1+result2+result1.rstrip()
print(put(k))

import math

# 定义函数f，它接收四个参数：n表示递归的深度，(x, y)表示在大矩阵中的位置，mp表示整个矩阵
def f(n, x, y, mp):
    # 基本情况：如果n为1，即递归到最深层，就在矩阵中的位置(x, y)放置'X'
    if n == 1:
        mp[x][y] = 'X'
    else:
        # 计算当前层的单位大小，每递归一层，单位大小变为原来的3倍
        unit = 3 ** (n - 2)
        # 递归调用f函数，分别在左上、右上、中间、左下、右下的位置填充子三角形
        f(n - 1, x, y, mp)                         # 左上
        f(n - 1, x, y + 2 * unit, mp)              # 右上
        f(n - 1, x + unit, y + unit, mp)           # 中间
        f(n - 1, x + 2 * unit, y, mp)              # 左下
        f(n - 1, x + 2 * unit, y + 2 * unit, mp)   # 右下


# 定义主函数main
def main():
    # 从用户那里获取输入，即递归的深度n
    n = int(input())
    # 计算边缘长度，Sierpinski三角形的每边长度是3的(n-1)次方
    edge = 3 ** (n - 1)
    # 初始化一个边缘长度为edge的正方形矩阵，所有元素初始化为空格' '
    mp = [[' ' for _ in range(edge)] for _ in range(edge)]
    # 从最顶层开始递归调用函数f，填充整个矩阵
    f(n, 0, 0, mp)

    # 遍历矩阵的每一行，将每行的元素连接成字符串，并打印出来
    for row in mp:
        print(''.join(row))


# 检查是否为主模块运行，如果是，则执行主函数main
if __name__ == "__main__":
    main()