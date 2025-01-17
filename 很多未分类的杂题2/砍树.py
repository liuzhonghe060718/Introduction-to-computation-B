n=int(input())
k=2
s = [[int(x) for x in input().split()] for i in range(n)]
if n==1:
    print(1)
else:
    for i in  range(1,n-1):
        if s[i][0]-s[i-1][0]>s[i][1]:
            k+=1
        elif s[i+1][0]-s[i][0]>s[i][1]:
            k+=1
            s[i][0]+=s[i][1]
    print(k)




