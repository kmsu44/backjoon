from collections import deque
m, n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]



raw_tomato = set()
q = deque()


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            raw_tomato.add((i,j))
        if graph[i][j] == 1:
            q.append((i,j,0))


moves = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def find_min_day():
    if len(raw_tomato) == 0:
        return 0
    while q:
        x,y,day = q.popleft()
        for xx, yy in moves:
            dx = xx + x
            dy = yy + y
            if in_range(dx,dy) and graph[dx][dy] == 0:
                graph[dx][dy] = 1
                raw_tomato.remove((dx,dy))
                if len(raw_tomato) == 0:
                    return day+1
                q.append((dx,dy,day+1))
    return -1

print(find_min_day())