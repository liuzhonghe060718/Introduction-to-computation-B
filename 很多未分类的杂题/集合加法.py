n=int(input())
for _ in range(n):
    answer=0
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b=int(input())
    B=list(map(int, input().split()))
    for x in A:
        if s-x in B:
            answer+=B.count(s-x)
    print(answer)