n=int(input())
numbers=[]
triple=[i**3 for i in range(n)]
for a in range(6,n):
    for d in range(5,a):
        for c in range(4,d):
            b=a**3-d**3-c**3
            if b in triple and b<c:
                    numbers.append([a,b,c,d])
for item in numbers:
    print(f'Cube = {item[0]}, Triple = ({item[1]},{item[2]},{item[3]})')

