import sys
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

dp = [sys.maxsize for _ in range(k+1)]
coins.sort()
dp[0] = 0
for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i-coin] + 1, dp[i])
    
if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
    
