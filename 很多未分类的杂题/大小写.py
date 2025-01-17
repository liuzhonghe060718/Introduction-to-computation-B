a=list(input())
s=[]
for i in a:
    b=i.isupper()
    if b:
        s.append(i.lower())
    else:
        s.append(i.upper())
print(''.join(s))