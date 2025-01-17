import math
s=input()
n=math.floor(math.log(len(s)+1,2))+1
ans=['']*n
for i in range(n):
    if i%2==0:
        ans[i]=s[2**(i//2)-1]
    else:
        ans[i]=s[2**(n-1-((i-1)//2))-1]
print(''.join(ans))