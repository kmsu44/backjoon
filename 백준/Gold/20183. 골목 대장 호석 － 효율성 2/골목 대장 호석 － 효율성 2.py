import sys
from collections import deque
input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

res = sys.maxsize


def BFS(start, end):
    global res
    q = deque()
    q.append((start, 0, 0))
    visit = [-1 for _ in range(n+1)]
    while q:
        now_pos, now_money, max_money = q.popleft()
        if now_money > c:
            continue
        if max_money > res:
            continue
        if now_pos == end:
            res = min(res, max_money)
            continue
        for next_pos, weight in graph[now_pos]:
            if visit[next_pos] == -1:
                visit[next_pos] = False
                q.append((next_pos, now_money + weight,
                          max(max_money, weight)))
    return -1


BFS(a, b)
if res == sys.maxsize:
    print(-1)
else:
    print(res)
