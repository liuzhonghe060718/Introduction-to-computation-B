n=int(input())
def u(n):
    i=2
    fen_jie=[]
    while n!=1:
        if n%i==0:
            n=n//i
            fen_jie.append(i)
        else:
            i+=1
    s=set(fen_jie)
    if len(s)<len(fen_jie):
        return 0
    if len(fen_jie)%2==0:
        return 1
    else:
        return -1
print(u(n))



###附加一个分解质因数的函数
#def pFactors(n):
 #   """Finds the prime factors of 'n'"""
   # from math import sqrt
   # pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

   # for check in range(2, limit):
   #     while num % check == 0:
     ##       pFact.append(check)
     #       num /= check
  #  if num > 1:
      #  pFact.append(num)
   # return pFact
