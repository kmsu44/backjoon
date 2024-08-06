from collections import deque
r, c = map(int,input().split())

graph = [list(input()) for _ in range(r)]

q = deque()


for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append((i,j,'*',0))
        if graph[i][j] == 'S':
            hedgehog = (i,j,'S',0)
        if graph[i][j] == 'D':
            goal = (i,j)

q.append(hedgehog)

moves = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]
def in_range(x,y):
    return 0 <= x < r and 0 <= y < c


def is_possible():
    while q:
        x,y,type,cnt = q.popleft()
        for xx, yy in moves:
            dx = x + xx
            dy = y + yy
            if type == 'S' and (dx,dy) == goal:
                return cnt+1
            if in_range(dx,dy) and graph[dx][dy] == '.' :
                if type =='*':
                    graph[dx][dy] = '*'
                if type == 'S':
                    graph[dx][dy] = 'S'
                q.append((dx,dy,type,cnt+1))
            
    return -1
    


cnt = is_possible()

if cnt == -1:
    print('KAKTUS')
else:
    print(cnt)