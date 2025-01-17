n=int(input())
pairs = [i[1:-1] for i in input().split()]
distance = [ sum(map(int,i.split(','))) for i in pairs]
price=list(map(int,input().split()))
rate=[]
ans=0
prices=sorted(price)
for i in range(n):
    rate.append((distance[i]/price[i],i))
rate.sort(reverse=True)
if n%2==0:
    ra=(rate[n//2][0]+rate[n//2-1][0])/2
    pt=(prices[n//2]+prices[n//2-1])/2

else:
    ra=rate[n//2][0]
    pt=prices[n//2]

for i in range(n):
    if rate[i][0]<=ra:
        break
    if price[rate[i][1]]<pt:
        ans+=1
print(ans)
