n=int(input())
a1_a2_a3=list(range(0,3*n+1,5))
i=-1
result=-1
while result==-1:
    he=a1_a2_a3[i]
    if he==0:
        break
    else:
        for a2 in range(0,n+1):
            if a2%2==0:
                a=0
            else:
                a=1
            for a1 in range(a,max(0,he-a2),2) :
                if (he-a1)%3==0:
                    result=he
                    break
        i-=1
print(result)


#无语死了，答案用这个笨蛋办法
# n = int(input())
# m=0
# for i in range(n, -1, -1):
#     for j in range(n, -1, -1):
#         for k in range(n, -1, -1):
#             if (i + j) % 2 == 0 and (j + k) % 3 == 0 and (i + j + k) % 5 == 0:
#                 m=max(m,i+j+k)
# print(m)