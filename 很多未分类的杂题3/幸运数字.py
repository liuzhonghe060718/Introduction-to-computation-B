number=int(input())
s=[4,7,44,77,47,74,444,447,474,744,774,747,477,777]
for i in s:
    if number%i==0:
        print("YES")
        break
    else:
        if i==777:
             print("NO")




