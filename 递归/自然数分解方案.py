def f(n, bound, memo={}):
    # 基本情况：如果n小于等于1或者没有可选的数字（bound小于等于0），返回0
    if n <= 1 or bound <= 0:
        return 0
    # 如果结果已经在memo中，直接返回
    if (n, bound) in memo:
        return memo[(n, bound)]
    else:
        ans = 0
        # 遍历所有可能的i值，从1到bound
        for i in range(1, bound + 1):
            # 递归计算使用i及以下的数字形成n-i的方式数量，并累加到ans
            ans += f(n - i, i, memo)
            # 如果n-i是一个有效的选择（即n-i大于0，且小于等于i，且小于等于bound），则增加一个方式
            if n - i > 0 and n - i <= i and n - i <= bound:
                ans += 1
        # 将计算结果存储在memo中，并返回
        memo[(n, bound)] = ans
        return ans

def main():
    # 从用户那里获取输入，即n的值
    n = int(input())
    # 调用函数f，并打印结果
    print(f(n, n - 1))

# 检查是否为主模块运行，如果是，则执行主函数main
if __name__ == "__main__":
    main()


def f(n, bound):
    if n <= 1 or bound <= 0:
        return 0
    ans = 0
    for i in range(1, bound + 1):
        ans += f(n - i, i)  # 递归调用，计算将 n - i 拆分为不超过 i 的正整数之和的方案数量
        if n - i > 0 and n - i <= i:
            ans += 1  # 如果 n - i 是一个正数且不超过 i，则增加一个额外的方案
    return ans

def main():
    n = int(input())
    print(f(n, n - 1))  # 启动递归过程，n - 1 作为初始的 bound 值

if __name__ == "__main__":
    main()