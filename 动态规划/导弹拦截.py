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
input()
s=list(map(int,input().split()))
print(min_testers_needed(s))