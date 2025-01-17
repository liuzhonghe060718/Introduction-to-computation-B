n=int(input())
last_1,last_2,number=1,2,0
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(n-2):
        number=last_2+last_1
        last_1=last_2
        last_2=number
    print(number%10007)

MOD = 10007
MAXN = 10000 + 1


def fibonacci(n):
    # 初始化数组
    fib = [0] * MAXN
    fib[1] , fib[2] = 1,2

    # 填充数组
    for i in range(3, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

    # 返回结果
    return fib[n]


# 读取输入
n = int(input())
# 输出结果
print(fibonacci(n))