import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
A = list((map(int, input().split())))

Memo = [0] * n
Memo[0] = x + A[0]

for i in range(1, n):
    Memo[i] = Memo[i-1] + A[i]
count = [0 for _ in range(n+1)]
if Memo[0] < k:
    count[1] = 1
for i in range(2, n+1):
    if Memo[i-1] < k:
        count[i] = count[i-1] + 1
    else:
        count[i] = count[i-1]
answer = []
for _ in range(m):
    l, r = map(int, input().split())
    answer.append(count[r-1] - count[l-1])

for i in answer:
    print(i)
