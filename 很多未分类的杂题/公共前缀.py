n=int(input())
active,k=True,1
words=[0]*n
for i in range(n):
    words[i]=input()
while active:
    a=words[0][:k]
    for m in words:
        if m[:k]!=a:
            active=False
    k+=1
print(''if len(a)==1 else a[:-1])
