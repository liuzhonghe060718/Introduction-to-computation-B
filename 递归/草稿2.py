a=input()
n=len(a)
dp=[False]*(n+1)
squares = set()
i = 1
while i * i <= 10 ** 9:
    squares.add(i * i)
    i += 1
dp[0]=True
for i in range(1, n+1):
        for j in range(i):
            if dp[j] and int(a[j:i]) in squares:
                dp[i] = True
                break
print('Yes'if dp[-1]else 'No')