N, L = map(int, input().split())
mod= 10 ** 9 + 7

dp = [1]

for i in range(1,N+1):
    if i < L:
        dp.append(dp[i-1])
    else:
        dp.append(dp[i-1] + dp[i-L])

ans = dp[N] % mod

print(ans)