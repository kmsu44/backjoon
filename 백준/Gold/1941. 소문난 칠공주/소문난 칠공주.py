from collections import deque

students = [list(input()) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
moves = [
    [0,1],
    [0,-1],
    [-1,0],
    [1,0]
]
ans = 0

def dfs(n, g_cnt,s_cnt):
    global ans
    if g_cnt > 7:
        return
    if n == 25:
        if g_cnt == 7 and s_cnt >= 4:
            if check():
                ans += 1
        return
    x,y = n // 5, n % 5
    visited[x][y] = 1
    dfs(n+1, g_cnt+1, s_cnt + int(students[x][y] == 'S'))
    visited[x][y] = 0
    dfs(n+1, g_cnt, s_cnt)

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i,j)


def in_range(x,y):
    return 0 <= x < 5 and 0 <= y < 5

def bfs(i,j):
    q = deque()
    v = set()
    cnt = 1 
    q.append((i,j))
    v.add((i,j))
    while q:
        x,y = q.popleft()
        for xx, yy in moves:
            dx = x + xx
            dy = y + yy
            if in_range(dx,dy) and (dx,dy) not in v and visited[dx][dy] == 1:
                v.add((dx,dy))
                q.append((dx,dy))
                cnt += 1
    return cnt == 7


dfs(0,0,0)
print(ans)