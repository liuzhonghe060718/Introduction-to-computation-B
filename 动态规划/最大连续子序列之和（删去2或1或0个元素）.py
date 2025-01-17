def max_subarray_sum(n, a):
    maxValue = float('-inf')  # 初始化最大值为负无穷
    for i in range(n):
        maxValue = max(maxValue, a[i])  # 找出数组中的最大值
    if maxValue < 0:  # 如果最大值小于0，则最大子数组和就是最大值
        return maxValue
    else:
        dp = [[0, 0,0] for _ in range(n)]  # 初始化动态规划数组
        dp[0][0] = a[0]  # dp[0][0]表示包括第i个元素的最大子数组和
        dp[0][1] = 0 # dp[0][1]表示不包括第i个元素的最大子数组和
        dp[0][1]=0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + a[i], a[i])  # 包括当前元素的最优解
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + a[i])# 不包括当前元素的最优解
            dp[i][2]=max(dp[i-1][1],dp[i-1][2]+a[i])
        res = 0  # 初始化结果为0
        for i in range(n):
            res = max(res,max(dp[i][2], max(dp[i][0], dp[i][1])))  # 找出最大的子数组和
        return res  # 返回最大子数组和

# 读取输入
n = int(input())
a = [int(x) for x in input().split()]

# 计算并输出结果
print(max_subarray_sum(n, a))