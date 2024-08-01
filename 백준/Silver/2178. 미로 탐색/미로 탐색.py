from collections import deque
n, m = map(int,input().split())

graph = [list(input()) for _ in range(n)]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < m and graph[x][y] == '1'

moves = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]
def BFS():
    q = deque()
    q.append((0,0,1))
    visited = set()
    visited.add((0,0))
    while q:
        x,y,cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for xx,yy in moves:
            dx = x + xx
            dy = y + yy
            if in_range(dx,dy) and (dx,dy) not in visited:
                visited.add((dx,dy))
                q.append((dx,dy,cnt+1))
    return -1

print(BFS())