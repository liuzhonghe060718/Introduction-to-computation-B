import math
values=input().split()
n,m,a=values
N=math.ceil(int(n)/int(a))
M=math.ceil(int(m)/int(a))
x=M*N
print(x)
