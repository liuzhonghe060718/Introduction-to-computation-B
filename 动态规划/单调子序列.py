k=int(input())
s=list(map(int,input().split()))
s.reverse()
dp=[1]*k
for i in range(1,k):
        db=dp[:i].copy()
        while True:
            m=db.index(max(db))
            if s[m]<=s[i]:
                dp[i]=db[m]+1
                break
            else:
                del db[m]
            if not db:
                break
print(max(dp))


def longest_non_decreasing_subsequence(n, a):
    # 初始化 dp 数组，dp[i] 表示以 a[i] 结尾的最长非递减子序列的长度
    dp = [1] * n

    # 遍历每个元素 a[i]
    for i in range(n):
        # 遍历 a[i] 之前的所有元素 a[j]
        for j in range(i):
            # 如果 a[j] <= a[i]，则更新 dp[i]
            if a[j] <= a[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 返回 dp 数组中的最大值
    return max(dp)


# 读取输入
n = int(input())
a = list(map(int, input().split()))

# 输出结果
print(longest_non_decreasing_subsequence(n, a))


#LIS算法
from bisect import bisect_right

def min_testers_needed(scores):
    scores.reverse()  # 反转序列以找到最长下降子序列的长度
    lis = []  # 用于存储最长上升子序列

    for score in scores:
        pos = bisect_right(lis, score)  # 找到当前元素应插入的位置
        if pos < len(lis):
            lis[pos] = score  # 替换为新的更小的元素
        else:
            lis.append(score)  # 如果当前位置没有位置可以替换，添加新元素

    return len(lis)
