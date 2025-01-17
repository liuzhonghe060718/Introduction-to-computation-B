import math
n=int(input())
for i in range(n):
    x=int(input())
    a=int(math.log(x,2))
    answer=int((1+x)*x/2-2**(a+2)+2)
    print(answer)


