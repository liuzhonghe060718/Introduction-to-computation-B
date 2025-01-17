n=input()
numbers=input().split()
x,y=0,0
X=[]
Y=[]
for number in numbers:
    if int(number)%2==1:
        x+=1
        X.append(number)
    else:
        y+=1
        Y.append(number)
if x>y:
    answer=numbers.index(Y[0])+1
else:
    answer = numbers.index(X[0]) + 1
print(answer)