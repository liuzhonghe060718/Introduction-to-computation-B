from functools import cmp_to_key

# 自定义比较函数
def compare(a, b):
    # 返回值小于0表示 a 排在 b 前面，大于0表示 b 排在 a 前面
    return len(a) - len(b)

lst = ["apple", "banana", "kiwi", "pear"]
lst.sort(key=cmp_to_key(compare))
print(lst)
