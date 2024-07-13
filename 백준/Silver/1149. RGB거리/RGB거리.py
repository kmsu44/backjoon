n = int(input())

houses = [list(map(int,input().split())) for _ in range(n)]


dp = [[0 for _ in range(n)] for _ in range(3)]


dp[0][0] = houses[0][0]
dp[1][0] = houses[0][1]
dp[2][0] = houses[0][2]


        
for i in range(1,n):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + houses[i][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + houses[i][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) +  + houses[i][2]



print(min(dp[0][n-1],dp[1][n-1],dp[2][n-1]))