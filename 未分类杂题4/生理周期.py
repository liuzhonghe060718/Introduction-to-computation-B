t=0
while True:
    p,e,i,d=map(int,input().split())
    if p<0:
        break
    else:
        for x in range(1,655):
            m=x*33+i
            if (m-p)%23==0 and (m-e)%28==0:
                t+=1
                break
        print(f"Case {t}: the next triple peak occurs in {m-d} days.")
