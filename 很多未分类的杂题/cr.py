s = input()
s = s.lower()

dp = [0] * 5
data = 'hello'
cnt = 0

for c in s:
    if c == data[cnt]:
        dp[cnt] += 1
        cnt += 1

    if cnt == 5:
        break

if sum(dp) == 5:
    print('YES')
else:
    print('NO')




import re
s = input()
r = re.search('h.*e.*l.*l.*o', s)
print(['YES', 'NO'][r==None])