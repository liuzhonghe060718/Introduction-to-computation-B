
lines=[]
while True:
    line=input()
    if line=="0.00":
        break
    else:
        lines.append(line)
for a in lines:
    i,sum=1,0
    while True:
        i+=1
        sum+=1/i
        if sum>=float(a):
            b=i-1
            print(f"{b} card(s)")
            break
        else:
            continue

