n=int(input())
prime=[0 for _ in range(10**6+1)]
common=[]
for i in range(2,10**6):
    if prime[i]==0:
        common.append(i)
    for j in common:
        if i*j>10**6:
            break
        prime[i*j]=1
        if j!=1 and i%j==0:
            break
common=set(common)
list_1=input().split()
for x in list_1:
    y=int(x)**(0.5)
    if int(y)-y!=0 or int(x)<=2 or y not in common:
            print('NO')
    else:
        print('YES')




