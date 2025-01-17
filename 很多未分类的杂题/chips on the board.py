text_numbers=int(input())
for i in range(text_numbers):
    n=int(input())
    hang=list(map(int,input().split()))
    lie = list(map(int, input().split()))
    a=n*min(hang)+sum(lie)
    b=n*min(lie)+sum(hang)
    print(min(a,b))