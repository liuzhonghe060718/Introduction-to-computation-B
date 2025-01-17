n=int(input())
i=0
liste=[]
while True:
    m=int(input())
    liste.append(m)
    i+=1
    if i==n:
        break
def cheak(a):
    a=int(a)
    t,c,d,e=0,0,0,a
    while e%2==0:
        e=e/2
        d+=1
    while e%3==0:
        e=e/3
        c+=1
    if e!=1 or c<d:
        return -1
    else:
        return 2*c-d
for x in liste:
        print(cheak(x))

