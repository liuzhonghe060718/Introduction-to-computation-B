n,x,y,z=map(int,input().split())
s=0
x,z,y=sorted([x,y,z])
for i in range(n//x+1):
    for j in range((n-i*x)//z+1):
        k=n-i*x-j*z
        if k%y==0:
            s=max(s,i+j+k//y)
print(s)



n,a,b,c=map(int,input().split())
s = [0]+[float('-inf')]*n

for i in range(1,n+1):
    for j in (a,b,c):
        if i>=j:
            s[i]=max(s[i],s[i-j]+1)
print(s[n])