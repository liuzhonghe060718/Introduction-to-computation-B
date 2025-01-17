t=int(input())
m=[]
for i in range(1,t+1):
    i+=1
    n,k=input().split()
    list_1=[int(a) for a in input().split()]
    list_2=sorted([int(a) for a in input().split()])
    list_3=sorted([(list_1[i],i)for i in range(n)])
