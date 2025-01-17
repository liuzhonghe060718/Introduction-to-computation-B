n,k=map(int,input().split())
bird=sorted(list(map(int,input().split())),reverse=True)
s4,s2=n,2*n
ans='YES'
for i in range(k):
    a=bird[i]//4
    if s4==0:
        break
    if a<=s4:
        bird[i]-=4*a
        s4-=a
    else:
        bird[i]-=4*s4
        s4=0
        break
if s4==0:
    for i in range(k):
        if bird[i]%2==1:
            s2-=(bird[i]//2+1)
        else:
            s2-=bird[i]//2
        if s2<0:
            ans='NO'
            break
else:
    kong1,kong2=0,0
    for i in range(k):
        if bird[i]==3:
            if s4>0:
                s4-=1
            else:
                s2-=2
        elif bird[i]==2:
            if kong2>0:
                kong2-=1
            elif s2>0:
                s2-=1
            else:
                s4-=1
                kong1+=1
        elif bird[i]==1:
            if kong1>0:
                kong1-=1
            elif s2>0:
                s2-=1

            else:
                s4-=1
                kong2 += 1
        if s2 < 0 or s4 < 0:
            ans='NO'
            break
print(ans)
