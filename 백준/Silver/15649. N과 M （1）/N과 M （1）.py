n, m = map(int, input().split())

L = [i for i in range(n+1)]

visit = [True for _ in range(n+1)]


def dfs(index, cnt, route):
    if cnt == m:
        print(route)
    for i in range(1, n+1):
        if visit[i]:
            visit[i] = False
            dfs(i, cnt+1, route + str(i)+' ')
            visit[i] = True


dfs(0, 0, '')
