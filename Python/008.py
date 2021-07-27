N = int(input())
S = input()   

T = "atcoder"

mod = 10 ** 9 + 7

dp = [[0 for i in range(len(T) + 1)] for j in range(len(S)+1)]

for i in range(len(S)+1):
    dp[i][0] = 1   

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i][j+1]

print(dp[len(S)][len(T)] % mod)