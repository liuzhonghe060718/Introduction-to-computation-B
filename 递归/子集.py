n1=int(input())
def zi(n):
    if n==1:
        return [[1]]
    else:
        s=[]
        for i in zi(n-1):
            s.append(i+[n])
        return zi(n-1)+s+[[n]]
print()
s=zi(n1)
s.sort(key=lambda a:(len(a),a))
for x in s:
    print(' '.join(map(str,x)))
