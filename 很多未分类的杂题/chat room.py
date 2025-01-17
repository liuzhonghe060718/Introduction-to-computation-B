s=list(input())
try:
    a=s.index("h")
    e=s.index("e")
    b=s.index("l")
    c=s.index("l",b+1)
    d=s.index("o")
except:
    print("NO")
else:
    if a<e<b<c<d:
        print("YES")
    else:
        print("NO")



