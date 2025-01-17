n=int(input())
values=list(map(int,input().split()))
values_2=sorted(values)
m=int(input())
for _ in range(m):
    x,l,r=map(int,input().split())
    if x==1:
        print(sum(values[l-1:r]))
    if x==2:
        print(sum(values_2[l-1:r]))



def precompute_prefix_sums(arr):
    prefix_sums = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i - 1]
    return prefix_sums

# 读取输入
n = int(input().strip())
v = list(map(int, input().strip().split()))
m = int(input().strip())

# 预计算原始数组和排序数组的前缀和
original_prefix_sums = precompute_prefix_sums(v)
sorted_v = sorted(v)
sorted_prefix_sums = precompute_prefix_sums(sorted_v)

# 处理每个查询
results = []
for _ in range(m):
    query = list(map(int, input().strip().split()))
    q_type, l, r = query[0], query[1], query[2]
    if q_type == 1:
        result = original_prefix_sums[r] - original_prefix_sums[l - 1]
    else:
        result = sorted_prefix_sums[r] - sorted_prefix_sums[l - 1]
    results.append(result)

# 输出结果
for result in results:
    print(result)
