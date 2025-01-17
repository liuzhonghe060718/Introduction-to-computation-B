n,k=map(int,input().split())
p={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
yu=[]
while n!=0:
    a=n%k
    if a<=9:
        yu.append(str(a))
    else:
        yu.append(p[a])
    n=n//k
print(''.join(yu[::-1]))

‘’‘递归方法’‘’
def to_str(n, base):
# 定义⽤于转换的字符序列
    convert_string = "0123456789ABCDEF"
# 基准情形：如果 n ⼩于基数，则直接返回对应的字符
    if n < base:
        return convert_string[n]
    else:
        # 递归调⽤：先处理商，再处理余数
    # 通过延迟连接操作，确保结果的顺序是正确的
        return to_str(n // base, base) + convert_string[n % base]

