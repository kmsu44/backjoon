from collections import defaultdict
import heapq
import sys
n = int(input())
m = int(input())
buses = defaultdict(list)
for _ in range(m):
    v1, v2, w = map(int,input().split())
    buses[v1].append((w,v2))

start, end = map(int,input().split())
distance = [sys.maxsize for _ in range(n+1)]
distance[start] = 0

def dijkstra():
    q = []
    heapq.heappush(q,(0,start))
    while q:
        d,cur = heapq.heappop(q)
        if distance[cur] < d:
            continue
        for w, v in buses[cur]:
            next_distance = d + w
            if next_distance < distance[v]:
                distance[v] = next_distance
                heapq.heappush(q,(next_distance,v))

dijkstra()

print(distance[end])

