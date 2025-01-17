import math
k1,cx1,cy1=map(int,input().split())
key=[]
def put(m,n,x,y):
    answer=[(x+m,y+n),(x+2*m,y+2*n),(x+3*m,y+3*n),(x+3*m,y),(x,y+3*n)]
    key.extend(answer)
def divide(k,cx,cy):
    if k==4:
        put()
