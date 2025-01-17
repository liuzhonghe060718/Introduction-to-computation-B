n,k=map(int,input().split())
time=sorted(list(map(int,input().split())))
while sum(time)<k*time[-1] and k>0:
    time.pop()
    k-=1
print('%.3f' % (sum(time)/k))


