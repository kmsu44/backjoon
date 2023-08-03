import sys
import heapq
inp = sys.stdin.readline
n, m, start, end, bank = map(int, inp().split())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
max_val = [INF] * (n+1)


def dijkstra(start):
    q = []
    distance[start] = 0
    max_val[start] = 0
    heapq.heappush(q, (0, start, 0))
    while q:

        dist, now, prev = heapq.heappop(q)
        # print(now)
        if distance[now] < dist:
            continue
        for next_node in graph[now]:
            if next_node[0] == prev:
                continue
            cur_cost = max_val[now] + next_node[1]
            if cur_cost > bank:
                # print('터짐')
                continue
            elif next_node[1] < distance[next_node[0]]:
                tmp = min(
                    max(next_node[1], distance[now]), distance[next_node[0]])
                if tmp == distance[next_node[0]]:
                    continue
                else:
                    distance[next_node[0]] = tmp
                if now == end:
                    continue
                max_val[next_node[0]] = cur_cost
                heapq.heappush(q, (next_node[1], next_node[0], now))


for _ in range(m):
    s, e, c = map(int, inp().split())
    graph[s].append((e, c))
    graph[e].append((s, c))
dijkstra(start)
# print(distance)
# print(max_val)
if distance[end] == INF:
    print(-1)
else:
    print(distance[end])


# 7 7 1 6 500
# 1 2 7
# 2 3 9
# 2 5 6
# 3 6 8
# 1 4 7
# 4 5 6
# 5 6 5


# 5 5 1 3 1000
# 1 2 5
# 2 3 5
# 1 4 2
# 4 5 6
# 5 3 2
