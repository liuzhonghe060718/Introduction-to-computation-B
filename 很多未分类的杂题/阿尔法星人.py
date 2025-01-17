
word=input().split()
k=1
number=0
def he(a):
    n2 = {'hundred': 100, 'thousand': 1000, 'million': 1000000}
    n1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
          'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
          'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
          'seventy': 70, 'eighty': 80, 'ninety': 90}
    s,n,p=0,0,1000000
    for x in a:
        if x not in n2.keys():
            s+=n1[x]
        else:
            if p >= n2[x]:
                n += s * n2[x]
                p = n2[x]
                q = s* n2[x]
                s=0
            else:
                n -= q
                n += (q + s) * n2[x]
                s= 0
    return n+s
if word==['zero']:
    print(0)
else:
    su=0
    for x in word:
        if x=='negative':
            k=-1
            del word[0]
            continue
        if 'million' in word:
            a = word.index('million')
            number = he(word[:a])*1000000+he(word[a+1:])
        else:
            number=he(word)
    print(k*number)



#one thousand three hundred fifty two million three hundred thousand four hundred two