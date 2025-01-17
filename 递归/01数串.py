n=int(input())
def ad(n):
    if n==1:
        return ['0','1']
    else:
        dm=[]
        for x in ad(n-1):
            for j in ['0','1']:
                dm.append(x+j)
        return dm
for a in ad(n):
    print(a)


def generate_binary_strings(n):
    result = []
    temp = []

    def DFS(idx):
        if idx == n:  # 终止条件：当处理到最后一个位置时
            result.append(temp[:])  # 将当前的01串添加到结果列表中
            return

        temp.append(0)  # 尝试在当前位置填入0
        DFS(idx + 1)  # 递归处理下一个位置
        temp.pop()  # 回溯：移除当前位置的值

        temp.append(1)  # 尝试在当前位置填入1
        DFS(idx + 1)  # 递归处理下一个位置
        temp.pop()  # 回溯：移除当前位置的值

    DFS(0)  # 从第一个位置开始递归

    # 输出所有可能的01串
    for binary_string in result:
        print("".join(map(str, binary_string)))


# 示例调用
generate_binary_strings(int(input()))