import math

n=int(input())
groups=list(map(int,input().split()))
s=[groups.count(1),groups.count(2),groups.count(3),groups.count(4)]
s[0]=max(s[0]-s[2]-2*(s[1]%2),0)
print(s[3]+s[2]+math.ceil(s[1]/2)+math.ceil(s[0]/4))
