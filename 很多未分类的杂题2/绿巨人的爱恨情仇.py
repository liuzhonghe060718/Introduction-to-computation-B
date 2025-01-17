n=int(input())
str_1="I hate"
str_2="I love"
answer=[]
for i in range(n):
    if i%2==0:
        answer.append(str_1)
    else:
        answer.append(str_2)
m=" that ".join(answer)
print(m,end=" it")

