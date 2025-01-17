n=int(input())
word=[]
for i in range(4):
    word.append(list(input()))
def check(x,idx,used):
    if idx==len(x):
        return True
    for s in word:
        if s not in used and x[idx] in s:
            if check(x,idx+1,used+[s]):
                return True
    return False
for _ in range(n):
    print('YES'if check(input(),0,[]) else 'NO')