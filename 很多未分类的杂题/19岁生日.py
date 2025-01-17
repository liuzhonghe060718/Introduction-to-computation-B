n=int(input())
def find(x:str):
    if int(x)%19==0 or '19' in x:
        return True
    return False
for _ in range(n):
    if find(input()):
        print('Yes')
    else:
        print('No')