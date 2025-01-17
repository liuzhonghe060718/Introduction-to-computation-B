def to_num(nums):
    return int(nums)


def dfs(nums):
    sum_result = to_num(nums)  # 初始结果为不插入加号时的结果
    count = 1  # 初始方案数为1

    for i in range(1, len(nums)):
        left_nums = nums[:i]  # 左边的部分
        right_nums = nums[i:]  # 右边的部分
        right_result = dfs(right_nums)  # 递归处理右边的部分
        sum_result += right_result[0] + right_result[1] * to_num(left_nums)  # 累加结果
        count += right_result[1]  # 累加方案数

    return (sum_result, count)


def main():
    nums = input().strip()
    print(dfs(nums)[0])
