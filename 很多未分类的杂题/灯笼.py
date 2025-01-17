n,l=map(int,input().split())
places=list(set(sorted(list(map(int,input().split())))))
answers=[0]*(n-1)
for i in range(n-1):
    a=places[i+1]-places[i]
    answers[i]=a
answer_1=(max(answers))/2
answer_2=max(places[0],l-places[-1])
print(f"{(max(answer_1,answer_2)):.10f}")