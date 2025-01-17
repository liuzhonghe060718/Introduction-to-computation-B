all_list=[]
for i in range(0,5):
    a=list(map(int, input().split()))
    all_list.append(a)
    if a!=[0,0,0,0,0]:
        m=i
n=all_list[m].index(1)
print(abs(n-2)+abs(m-2))
