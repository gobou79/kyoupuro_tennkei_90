N, K = map(int, input().split())

ans = 0
mod = 10 ** 9 + 7

if K > 2 and N > 1:
    ans = (K * (K-1) * pow(K-2, N-2, mod)) % mod
    print(ans)
elif N == 1:
    print(K)
elif K == 2 and N == 2:
    print(2)
else:
    print(0)