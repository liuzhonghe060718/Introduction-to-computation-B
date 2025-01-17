def moveHanoi(n, from_rod, to_rod, mid_rod):
    if n == 0:
        return
    moveHanoi(n - 1, from_rod, mid_rod, to_rod)
    print(f"{from_rod}->{to_rod}")
    moveHanoi(n - 1, mid_rod, to_rod, from_rod)
n = int(input())
print(2**n - 1)
moveHanoi(n, 'A', 'C', 'B')