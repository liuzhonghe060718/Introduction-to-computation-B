from collections import deque
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(w,h,martix,x1,y1,x2,y2):
    queue=deque([])
    queue.extend([[(x1,y1),0,'x'],[(x1,y1),0,'y']])
    visited=[[False]*(w+2) for _ in range(h+2)]
    while queue:
        (dx,dy),steps,dire=queue.popleft()
        visited[dx][dy]=True
        if dire=='y':
            for i in range(1,dx+1):
                nx=dx-i
                if nx==x2 and dy==y2:
                    return steps+1
                if nx<0 or martix[nx][dy]!=' ':
                    break
                if not visited[nx][dy]:
                    queue.append([(nx,dy),steps+1,'x'])
            for i in range(1,h-dx+2):
                nx=dx+i
                if nx==x2 and dy==y2:
                    return steps+1
                if nx>=h+2 or martix[nx][dy]!=' ':
                    break
                if not visited[nx][dy]:
                    queue.append([(nx,dy),steps+1,'x'])
        else:
            for i in range(1, dy + 1):
                ny = dy - i
                if dx==x2 and ny==y2:
                    return steps+1
                if ny<0 or martix[dx][ny] != ' ':
                    break
                if not visited[dx][ny]:
                    queue.append([(dx, ny), steps+1, 'y'])
            for i in range(1, w - dy + 2):
                ny = dy + i
                if dx==x2 and ny==y2:
                    return steps+1
                if ny>=w+2 or martix[dx][ny] != ' ' :
                    break
                if not visited[dx][ny]:
                    queue.append([(dx, ny), steps+1, 'y'])
    return False
k0=1
while True:
    w1,h1=map(int,input().split())
    if w1==h1==0:
        break
    print(f'Board #{k0}:')
    grid=[' '*(w1+2)]
    for _ in range(h1):
        grid.append(' '+input()+' ')
    grid.append(' '*(w1+2))
    k1=1
    while True:
        X1,Y1,X2,Y2=map(int,input().split())
        if X1==X2==Y1==Y2==0:
            break
        a=bfs(w1,h1,grid,Y1,X1,Y2,X2)
        if a:
            print(f'Pair {k1}: {a} segments.')
        else:
            print(f'Pair {k1}: impossible.')
        k1+=1
    k0+=1
    print('')