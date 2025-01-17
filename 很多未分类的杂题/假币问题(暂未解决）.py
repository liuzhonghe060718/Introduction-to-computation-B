n=int(input())
money={'A','B','C','D','E','F','G','H','I','J','K','L'}

def check(x,real1):
    if x[2]=={'e','n','v'}:
        real1.update(x[0]|x[1])
    if x[2]=={'u','p'}:
        x[0],x[1]=x[1],x[0]
    return x

for _ in range(n):
    final_answer=[]
    answer = ['0', '0']
    real=set()
    a=[set(i)for i in input().split()]
    b = [set(i)for i in input().split()]
    c = [set(i)for i in input().split()]
    A=check(a,real)
    B=check(b,real)
    C=check(c,real)
    wrong=money-real
    for i in wrong:
        answer = ['0', '0']
        for j in [A,B,C,[]]:
            if not j:
                final_answer = answer
                break
            if j[2]=={'e','n','v'}:
                continue
            if i in j[0]:
                if answer==[i,'light'] or answer==['0','0']:
                    answer =[i, 'light']
                else:
                    break
            elif i in j[1]:
                if answer==[i,'heavy'] or answer==['0','0']:
                    answer =[i, 'heavy']
                else:
                    break
            else:
                break
    print(f'{final_answer[0]} is the counterfeit coin and it is {final_answer[1]}.')





