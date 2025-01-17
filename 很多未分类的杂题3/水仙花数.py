a,b=list(map(int,input().split()))
answer=[]
for i in range(a,b+1):
    s=list(str(i))
    if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
        answer.append(i)
if answer==[]:
    print('NO')
else:
    print(' '.join([str(j)for j in answer]))