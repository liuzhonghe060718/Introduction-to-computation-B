def manacher(s):
    # 步骤 1: 转换字符串
    T = "#" + "#".join(s) + "#"
    n = len(T)

    # 步骤 2: 初始化回文半径数组
    P = [0] * n
    C = 0  # 回文中心
    R = 0  # 回文右边界
    max_len = 0  # 最长回文长度
    center_index = 0  # 最长回文串的中心位置

    # 步骤 3: 遍历字符串 T
    for i in range(n):
        # 步骤 4: 获取对称位置
        mirror = 2 * C - i

        # 步骤 5: 判断当前字符是否在回文边界内
        if i < R:
            P[i] = min(R - i, P[mirror])  # 通过对称性推导回文半径

        # 步骤 6: 尝试扩展回文
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # 步骤 7: 更新回文中心和右边界
        if i + P[i] > R:
            C = i
            R = i + P[i]

        # 步骤 8: 更新最长回文长度
        if P[i] > max_len:
            max_len = P[i]
            center_index = i

    # 步骤 9: 获取最长回文子串
    start = (center_index - max_len) // 2  # 注意转换回原始字符串的索引
    return s[start:start + max_len]


# 测试
s = "abadaba"
result = manacher(s)
print(result)  # 输出可能是 "bab" 或 "aba"，取决于实现细节

