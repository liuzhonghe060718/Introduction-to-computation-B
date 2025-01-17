n=int(input())
B=list(map(int,input().split()))
for i in range(n-1):
    if B[i]<=B[i+1]:
        if i==n-2:
            print("YES")
        continue
    else:
        print("NO")
        break
