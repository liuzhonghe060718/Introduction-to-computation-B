a_1,b_1=input().split()
A,B,C,E,F=[],[],[],[],[]
for i in range(int(a_1)):
    s=list(map(int,input().split()))
    A.append(s)
a_2,b_2=input().split()
for i in range(int(a_2)):
    s=list(map(int,input().split()))
    B.append(s)
a_3,b_3=input().split()

for i in range(int(a_3)):
    s=list(map(int,input().split()))
    C.append(s)
D=[[0 for j in range(int(b_3))] for i in range(int(a_3))]
if b_1!=a_2 or a_1!=a_3 or b_2!=b_3:
    print("Error!")
else:
    for i in range(int(a_1)):
        for j in range(int(b_2)):
            for k in range(int(b_1)):
                D[i][j]+=A[i][k]*B[k][j]
            D[i][j]+=C[i][j]
    for i in range(int(a_3)):
        print(' '.join([str(j) for j in D[i]]))
