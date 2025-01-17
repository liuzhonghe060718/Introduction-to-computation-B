s=[[False for _ in range(8)]for _ in range(8)]
answer,key=['0']*92,[]
def chu(i,j,ls):
    for x in range(8):
        ls[i][0]=True
    for x in range(8):
        ls[j][x]=True
    for x in range(i+j):
        ls[x][j+i-x]=True
m,n,t,k=0,0,0,0
while answer[-1]=='0':
    while len(key)<8 and m<8 and n<8:
        if not s[m][n]:
            chu(m,n,s)
            key.append(n)
            m+=1
            n=0
        else:
            n+=1
            if n==7:
                m+=1
                n=0
    if len(key)==8:
        answer[t]=''.join(map(str,key))
        t+=1
    key.clear()
    m,n=0,k
    k+=1
answer.sort()
print(answer)



