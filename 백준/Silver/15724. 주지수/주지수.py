import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
S = [[0] * (m+1) for _ in range(n)]

for i in range(n):
    for j in range(1, m+1):
        S[i][j] = S[i][j-1] + graph[i][j-1]
k = int(input())

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for row in range(x1-1, x2):
        res += S[row][y2] - S[row][y1-1]
    print(res)

# 4 4
# 9 14 29 7
# 1 31 6 13
# 21 26 40 16
# 8 38 11 23
# 3
# 1 1 3 2
# 1 1 1 4
# 1 1 4 4
