arr = [0] + list(map(int,input()))
size = len(arr)

dp = [0 for _ in range(size)]

if arr[1] == 0:
    print(0)
else:
    dp[0] = dp[1] = 1
    for i in range(2, size):
        if arr[i] > 0:
            dp[i] += dp[i-1]
        tmp = arr[i-1] * 10 + arr[i]
        if 10<= tmp <= 26:
            dp[i] += dp[i-2]
    print(dp[size-1] % 1000000)
