n = int(input())
calc, write = [], []
for _ in range(n):
    c, w = (int(x) for x in input().split())
    calc.append(c)
    write.append(w)
ans = day = 0
for c, w in sorted(zip(calc, write), key=lambda x: -x[1]):
    day += c
    ans = max(ans, day + w)
print(ans)