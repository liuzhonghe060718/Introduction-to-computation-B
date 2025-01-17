
def cheak(values):
    if values.count("@")!=1:
        return 'NO'
    if values.count(".")==0:
        return "NO"
    a=values.index("@")
    b=values.index(".")
    if a==0 or b==0 or a==len(values)-1 or values[-1]=="." or a==b-1 or a==b+1:
        return "NO"
    else:
        for i in values[a+1:]:
            if i==".":
                return "YES"
        return "NO"
while True:
    try:
        values=list(input())
        print(cheak(values))
    except EOFError:
        break

