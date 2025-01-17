x=int(input())
def cheak(n):
    n=int(n)
    if n<=2:
        return False
    if n%2==0:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n%i==0:
            return False
    return True
if x%2==1 or x<6:
    print("Error!")
else:
    for y in range(1,int(x/2)+1):
        y=int(y)
        z=x-y
        if cheak(str(y))==False or cheak(str(z))==False:
            pass
        else:
            print(f"{x}={y}+{z}".strip())




