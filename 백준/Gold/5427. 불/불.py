from collections import deque
t = int(input())




def get_queue(graph,w,h):
    q = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                q.append((i,j,'*',0))
            if graph[i][j] == '@':
                start_pos = (i,j,'@',0)
    q.append(start_pos)
    return q

def in_range(x,y,w,h):
    return 0 <= x < h and 0 <= y < w

moves = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]

def arrive(x,y,w,h):
    return x == 0 or x == h-1 or y == w-1 or y == 0

def is_possible(q,w,h):
    while q:
        x,y,type,cnt = q.popleft()
        if type == '@' and arrive(x,y,w,h):
            return cnt
        for xx,yy in moves:
            dx = x + xx
            dy = y + yy
            if in_range(dx,dy,w,h) and graph[dx][dy] == '.':
                if type == '*':
                    graph[dx][dy] = '*'
                else:
                    graph[dx][dy] = '@'                    
                q.append((dx,dy,type,cnt+1))
    return -1

def solution(graph,w,h):
    q = get_queue(graph,w,h)
    cnt = is_possible(q,w,h)
    if cnt == -1:
        return 'IMPOSSIBLE'
    else:
        return cnt + 1

ans = []
for _ in range(t):
    w,h = map(int,input().split())
    graph = [list(input()) for _ in range(h)]
    ans.append(solution(graph,w,h))
for i in ans:
    print(i)