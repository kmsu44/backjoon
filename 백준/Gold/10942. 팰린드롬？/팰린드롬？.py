import sys
input = sys.stdin.readline
n = int(input())
arr= [0] + list(map(int,input().split()))
t = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]



for i in range(1,n+1):
    dp[i][i] = 1
    if i+1 <= n:
        dp[i][i+1] = 1 if arr[i] == arr[i+1] else 0


for length in range(2,n+1):
    for left in range(1,n+1):
        if left + length > n:
            continue
        right = left + length
        if arr[left] == arr[right]:
            dp[left][right] = 1 if dp[left+1][right-1] else 0

for _ in range(t):
    start,end = map(int,input().split())
    print(dp[start][end])
