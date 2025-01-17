n=int(input())
all_people=sorted(list(map(int,input().split())))
if n<=2:
    print(n)
else:
    time=all_people[0]+all_people[1]
    people=2
    for x in all_people[2:]:
        if time<=x:
            people+=1
            time+=x
    print(people)


