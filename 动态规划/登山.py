n=int(input())
high=list(map(int,input().split()))
def find(s):
    dph=[1]*n
    for i in range(1,n):
        for j in range(i):
            if s[j]<s[i]:
                dph[i]=max(dph[i],dph[j]+1)
    return dph
s1=find(high)
s2=find(high[::-1])
s2.reverse()
answer=0
for i in range(n):
    answer=max(answer,s1[i]+s2[i]-1)
print(answer)

