from collections import defaultdict
import heapq
import sys

n, m = map(int,input().split())
start_vertex = int(input())

graph = defaultdict(list)

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


distance = [sys.maxsize for _ in range(n+1)]
distance[start_vertex] = 0

def dijkstra(graph):
    q = []
    heapq.heappush(q,(0,start_vertex))
    while q:
        d, cur = heapq.heappop(q)
        if distance[cur] < d:
            continue
        for v,w in graph[cur]:
            next_distance = d + w
            if next_distance < distance[v]:
                distance[v] = next_distance
                heapq.heappush(q,(next_distance,v))
dijkstra(graph)

for d in distance[1:]:
    if d == sys.maxsize:
        print('INF')
    else:
        print(d)