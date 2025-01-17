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
m=sorted(sorting(n))
for i in range(len(m)):
    print(' '.join(map(str,m[i])))


def dfs(idx, n, used, temp, result):
    if idx == n + 1:  # 如果当前位置已经是 n+1，说明已经生成了一个完整的全排列
        result.append(temp[:])  # 将当前排列添加到结果列表中
        return

    for i in range(1, n + 1):
        if not used[i]:  # 如果数字 i 还没有被使用过
            temp.append(i)  # 将数字 i 添加到当前排列中
            used[i] = True  # 标记数字 i 为已使用
            dfs(idx + 1, n, used, temp, result)  # 递归处理下一个位置
            used[i] = False  # 回溯：将数字 i 标记为未使用
            temp.pop()  # 回溯：将数字 i 从当前排列中移除


def generate_permutations(n):
    result = []
    used = [False] * (n + 1)  # 初始化 used 数组，用于标记数字是否被使用过
    dfs(1, n, used, [], result)  # 从第一个位置开始递归生成全排列

    for perm in result:
        print(" ".join(map(str, perm)))  # 按要求输出每个排列


# 读取输入
n = int(input())
generate_permutations(n)