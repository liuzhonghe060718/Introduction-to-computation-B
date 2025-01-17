def combination_sum(candidates, target, k, path, start, result):
    if len(path) == k and sum(path) == target:
        result.append(path[:])
        return
    if len(path) > k or sum(path) > target:
        return
    for i in range(start, len(candidates)):
        # 做选择
        path.append(candidates[i])
        # 递归
        combination_sum(candidates, target, k, path, i, result)
        # 撤销选择
        path.pop()

# 示例调用
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
k = 3
result = []
combination_sum(candidates, target, k, [], 0, result)
print(result)