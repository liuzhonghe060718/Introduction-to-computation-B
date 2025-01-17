

def generate_subsets(n,s):
    result = []
    temp = []

    def dfs(idx,s):
        if idx == n:
            result.append(tuple(temp[:]))  # 将当前子集加入结果集
            return
        temp.append(s[idx])  # 选择当前元素
        dfs(idx + 1,s)  # 递归处理下一个元素
        temp.pop()  # 不选择当前元素
        dfs(idx + 1,s)  # 递归处理下一个元素

    dfs(0,s)  # 从第一个元素开始递归生成子集
    result.sort(key=lambda x: (len(x), x))  # 按元素个数和字典序排序
    return result

n = int(input())
s1=list(map(int,input().split()))
subsets = list(set(generate_subsets(n,s1)))
for subset in subsets:
    print(" ".join(map(str, subset)))  # 输出子集，元素之间用空格隔