s = input()
n = int(input())

words = [input() for _ in range(n)]


dp = [0 for _ in range(len(s)+1)]
dp[0] = 1
for start in range(len(s)):
    if dp[start] == 0: continue
    for word in words:
        word_size = len(word)
        end = start + word_size
        if end > len(s):
            continue
        tmp = s[start:end]
        if tmp == word:
            dp[start+word_size] = 1
    

print(dp[len(s)])