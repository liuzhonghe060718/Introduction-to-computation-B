import math
n=int(input())
i=0
while i<n:
    a,b,c=list(map(float,input().split()))
    der=b*b-4*a*c
    if b==0:
        b=-b
    if der==0:
        answer=-b/(2*a)
        if answer!=0:
            print(f"x1=x2={answer:.5f}")
        else:
            print("x1=x2=0.00000")
    elif der>0:
        e=(-b+math.sqrt(der))/(2*a)
        d= (-b - math.sqrt(der)) / (2 * a)
        x1=max(e,d)
        x2=min(e,d)
        print(f"x1={x1:.5f};x2={x2:.5f}")
    else:
        e=(math.sqrt(0-der))/(2*a)
        d=-b/(2*a)
        if a>0:
            print(f"x1={d:.5f}+{e:.5f}i;x2={d:.5f}-{e:.5f}i")
        else:
            print(f"x1={d:.5f}-{e:.5f}i;x2={d:.5f}+{e:.5f}i")
    i+=1