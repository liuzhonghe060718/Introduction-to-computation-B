from math import gcd

while True:
    try:
        a, b = input().split()
        print(gcd(int(a), int(b)))
    except EOFError:
        break
