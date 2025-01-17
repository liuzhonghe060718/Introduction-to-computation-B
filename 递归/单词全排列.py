def dfs(idx, n, used, temp, result,s):
    if idx == n:  # 如果当前位置已经是 n+1，说明已经生成了一个完整的全排列
        result.append(''.join(temp[:]))  # 将当前排列添加到结果列表中
        return

    for i in range(n ):
        if not used[i]:  # 如果数字 i 还没有被使用过
            temp.append(s[i])  # 将数字 i 添加到当前排列中
            used[i] = True  # 标记数字 i 为已使用
            dfs(idx + 1, n, used, temp, result,s)  # 递归处理下一个位置
            used[i] = False  # 回溯：将数字 i 标记为未使用
            temp.pop()  # 回溯：将数字 i 从当前排列中移除


def generate_permutations(n,s):
    result = []
    used = [False] * (n + 1)  # 初始化 used 数组，用于标记数字是否被使用过
    dfs(0, n, used, [], result,s)  # 从第一个位置开始递归生成全排列

      # 按要求输出每个排列
    result.sort()
    for x in result:
        print(x)

# 读取输入
p=list(input())
n=len(p)
generate_permutations(n,p)