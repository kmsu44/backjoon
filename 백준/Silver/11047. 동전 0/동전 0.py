n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
ans = 0
for coin in coins[::-1]:
    if k == 0:
        break
    q,r = divmod(k,coin)
    if q != 0:
        ans += q
    k = r
print(ans)