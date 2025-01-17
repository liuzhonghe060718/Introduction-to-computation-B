x=int(input())
while x!=1:
    if x%2==0:
        x1=int(x/2)
        print(f"{x}/2={x1}")
        x=x1
    else:
        x2=x*3+1
        print(f"{x}*3+1={x2}")
        x=x2