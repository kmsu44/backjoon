def min_insertions_to_make_palindrome(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]

n = int(input())
arr = list(map(int, input().split()))
print(min_insertions_to_make_palindrome(arr))