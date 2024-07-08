n = int(input())
assignments = [list(map(int,input().split())) for _ in range(n)]
assignments.sort(key = lambda x:-x[1])
ans = 0
visited = set()

for d,w in assignments:
    while d > 0 and d in visited:
        d -= 1
    if d == 0:
        continue
    else:
        visited.add(d)
        ans += w
print(ans)