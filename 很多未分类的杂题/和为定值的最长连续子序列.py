# 示例输入 1
n = 6



gifts=[600, 400, 520, 520, 600, 440]
from collections import defaultdict

def find_max_value(n, gifts):
    target_average = 520
    # 计算需要的偏移量使得目标变为0
    gifts_offset = [x - target_average for x in gifts]

    prefix_sum = 0
    max_length = 0
    sum_indices = defaultdict(list)
    sum_indices[0].append(-1)  # 初始化，表示从开始到-1的和为0

    for i, gift in enumerate(gifts_offset):
        prefix_sum += gift
        if prefix_sum in sum_indices:
            # 如果当前前缀和之前出现过，说明存在一个子数组其元素平均值为target_average
            length = i - sum_indices[prefix_sum][0]  # 取最早的索引来获得最长的子数组
            max_length = max(max_length, length)
        sum_indices[prefix_sum].append(i)

    # 计算最大子数组的总和
    max_value = max_length * target_average if max_length > 0 else 0
    return max_value



# 计算结果
result = find_max_value(n, gifts)
print(result)



