def solution(triangle):
    answer = 0
    dp = []
    col = len(triangle) + 1
    row = len(triangle[-1]) + 1
    dp = [[0] * row for _ in range(row)]
    
    dp [1][1] = triangle[0][0]
    for i,idata in enumerate(triangle):
        for j,jdata in enumerate(idata):
            dp[i+1][j+1] = max(dp[i][j+1] + triangle[i][j], dp[i][j] + triangle[i][j])        
    return max(dp[-1])