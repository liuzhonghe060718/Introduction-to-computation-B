p=int(input())
s=["pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", "yax", "zac", "ceh", "mac",
                 "kankin", "muan", "pax", "koyab", "cumhu","uayet"]
t=["imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", "ok", "chuen", "eb",
                    "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"]
answer=[]
for _ in range(p):
    c,b,a=input().split()
    days=int(a)*365+s.index(b)*20+int(c[:-1])+1
    x=(days-1)//260
    days=days%260
    m=days%13
    n=days%20
    if m==0:
        m=13
    answer.append(f'{m} {t[n-1]} {x}')
print(p)
for i in answer:
    print(i)