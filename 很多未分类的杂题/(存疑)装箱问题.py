import math
def number(x):
    if x<=0:
        return 0
    else:
        return x
while True:
    s=list(map(int,input().split()))
    if sum(s)==0:
        break
    else:
        a,b,c,d,e,f=s
        n = f+e+d+(math.ceil(c/4))
        for i in range(e):
            a=a-11
            a=number(a)
        b-=5*d
        if b<0:
            b=0
            a=a-(20*d-4*b)
            a=number(a)
        m=4-c%4
        k=0
        if m!=0:
            a_1=a-(m+4)
            b_1=b-(2*m-1)
            a_1=number(a_1)
            b_1=number(b_1)
            k=math.ceil((4*b_1+a_1)/36)
            if m==2:
                a_2=a-10
                b_2=b-2
                a_2=number(a_2)
                b_2= number(b_2)
                k=min(math.ceil((4*b_1+a_1)/36),math.ceil((4*b_2+a_2)/36))
        s.clear()
        print(n+k)

