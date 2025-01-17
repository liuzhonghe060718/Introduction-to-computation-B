n=int(input())
i=0
liste=[]
while True:
    q=input()
    liste.append(q)
    i+=1
    if i==n:
        break
for x in liste:
    c=int(x[:2])
    y=int(x[2:4])
    m=int(x[4:6])
    d=int(x[6:])
    if m==1 or m==2:
        m+=12
        y=y-1
        if y==-1:
            y=99
            c=c-1
    t=26 * (m + 1)
    w=(y+y//4+c//4-2*c+t//10+d-1)%7
    week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    print(week[w])