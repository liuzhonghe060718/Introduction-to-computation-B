n=int(input())
nums=list(map(int,input().split()))
s1={}
s=[]
for x in nums:
    s1[x] = s1.setdefault(x, 0) + x
for a,b in s1.items():
    s.append([a,b])
m=len(s)
s.sort()
dp=[0for _ in range(m)]
dp[0]=s[0][1]
if m==1:
    print(dp[0])
else:
    if s[1][0]-s[0][0]>1:
        dp[1]=s[0][1]+s[1][1]
        m2=[s[1][0],dp[1]]
        m1=[s[0][0],dp[0]]
    else:
        dp[1]=s[1][1]
        if dp[0]<dp[1]:
            m2 = [s[1][0], dp[1]]
            m1 = [s[0][0], dp[0]]
        else:
            m1 = [s[1][0], dp[1]]
            m2 = [s[0][0], dp[0]]
    for x in range(2,m):
        dp[x]=s[x][1]
        if s[x][0]-m2[0]>1:
            dp[x]=m2[1]+s[x][1]
            m1=m2
            m2=[s[x][0],dp[x]]
        else:
            dp[x]=m1[1]+s[x][1]
            if m2[1]<dp[x]:
                m1=m2
                m2=[s[x][0],dp[x]]
            else:
                m1=[0,max(dp[x],m1[1])]
    print(max(dp))

n=int(input())
nums=list(map(int,input().split()))
dp=[0]*(10**5+1)
s=[]
for x in nums:
    dp[x]+=x
for i in range(10**5+1):
    if dp[i]!=0:
        s.append([i,dp[i]])
m=len(s)
s.sort()
dp=[0for _ in range(m)]
dp[0]=s[0][1]
if m==1:
    print(dp[0])
else:
    if s[1][0]-s[0][0]>1:
        dp[1]=s[0][1]+s[1][1]
        m2=[s[1][0],dp[1]]
        m1=[s[0][0],dp[0]]
    else:
        dp[1]=s[1][1]
        if dp[0]<dp[1]:
            m2 = [s[1][0], dp[1]]
            m1 = [s[0][0], dp[0]]
        else:
            m1 = [s[1][0], dp[1]]
            m2 = [s[0][0], dp[0]]
    for x in range(2,m):
        dp[x]=s[x][1]
        if s[x][0]-m2[0]>1:
            dp[x]=m2[1]+s[x][1]
            m1=m2
            m2=[s[x][0],dp[x]]
        else:
            dp[x]=m1[1]+s[x][1]
            if m2[1]<dp[x]:
                m1=m2
                m2=[s[x][0],dp[x]]
            else:
                m1=[0,max(dp[x],m1[1])]
    print(max(dp))

#服了，这个题错点在10**5，没加一导致那个数字输不上去太无语了，也是没想到第二种会更快