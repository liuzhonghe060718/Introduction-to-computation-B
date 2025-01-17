
n=int(input())
laptop={}
for _ in range(n):
    a,b=map(int,input().split())
    laptop[a]=b
laptops=sorted(laptop.items())
def check(result):
    for i in range(n-1):
        if laptops[i][1]>laptops[i+1][1]:
            result='Happy'
            return result
    return result
a=check('Poor')
print(f'{a} Alex')

