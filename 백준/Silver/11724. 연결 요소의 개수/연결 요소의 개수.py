from collections import defaultdict,deque
n, m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)



visited = set()

def BFS(v):
    q = deque()
    q.append(v)
    visited.add(v)
    while q:
        u = q.popleft()
        for vv in graph[u]:
            if vv not in visited:
                visited.add(vv)
                q.append(vv)

cnt = 0
for i in range(1, n+1):
    if i not in visited:
        cnt += 1
        BFS(i)
print(cnt)