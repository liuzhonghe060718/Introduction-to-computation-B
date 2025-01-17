text=list(input())
m=int(input())
x,answer=0,[0]
for i in range(1,len(text)):
    if text[i]==text[i-1]:
        x+=1
    answer.append(x)
for _ in range(m):
    l,r=map(int,input().split())
    print(answer[r-1]-answer[l-1])

