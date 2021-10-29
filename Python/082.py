l, r = input().split()
L = int(l)
R = int(r)

mod = 10 ** 9 + 7

ans = 0

for i in range(len(l), len(r)+1):
    if len(l) == len(r):
        ans += (L + R) * (R-L+1) * i // 2
        ans = ans % mod
    elif i == len(l):
        ans += (10 ** i - L) * (L + 10**i -1) * i // 2
        ans = ans % mod
    elif i == len(r):
        ans += (R - 10 ** (i-1) + 1) * (10**(i-1) + R) * i // 2
        ans = ans % mod
    else:
        ans += (10 ** i - 10 ** (i-1)) * (10 ** i + 10 ** (i-1) -1) * i // 2
        ans = ans % mod

print(ans)