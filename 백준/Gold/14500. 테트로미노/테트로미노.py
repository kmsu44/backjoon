import sys
input = sys.stdin.readline
# 시간제한 2초
# M = 500 -> O(N^3)가능
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = []

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]


def DFS(x, y, cnt, score):
    # 상 하 좌 우
    if cnt == 4:
        result.append(score)
        return
    for i in range(4):
        dx = nx[i] + x
        dy = ny[i] + y
        if 0 <= dx < n and 0 <= dy < m and visit[dx][dy]:
            visit[dx][dy] = False
            DFS(dx, dy, cnt+1, score + graph[dx][dy])
            visit[dx][dy] = True

    return 0


visit = [[True for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        # 길이가 4 DFS 탐색 -> ㅡ ㄴ ㅁ h 찾기
        visit[i][j] = False
        DFS(i, j, 1, graph[i][j])
        visit[i][j] = True
        # ㅏ
        if 0 < i < n-1 and 0 < j < m:
            result.append(graph[i][j] + graph[i]
                          [j-1] + graph[i+1][j-1] + graph[i-1][j-1])
        # ㅓ
        if 0 < i < n-1 and 0 <= j < m-1:
            result.append(graph[i][j] + graph[i]
                          [j+1] + graph[i+1][j+1] + graph[i-1][j+1])
        # ㅜ
        if 0 < i < n and 0 < j < m-1:
            result.append(graph[i][j] + graph[i-1]
                          [j] + graph[i-1][j-1] + graph[i-1][j+1])
        # ㅗ
        if 0 <= i < n-1 and 0 < j < m-1:
            result.append(graph[i][j] + graph[i+1]
                          [j] + graph[i+1][j+1] + graph[i+1][j-1])
result.sort(reverse=True)
print(result[0])
